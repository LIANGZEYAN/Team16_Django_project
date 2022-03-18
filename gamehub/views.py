import json

from django.core import serializers
from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from gamehub.bing_search import run_query
from gamehub.models import Game
from gamehub.models import Comment
from django.db.models import Count
from gamehub.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required



def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage matches to {{ boldmessage }} in the template!
    game_list1 = Game.objects.order_by('-views')[:3]
    # comments list
    form_of_comments = Comment.objects.values('game__name', 'game__slug', 'game__id').annotate(num_of_comments = Count('game')).order_by()
    
    result = []
    for i in form_of_comments:  
        result.append(i['game__name'])

    # print(form_of_comments)

    # search
    search_result = []
    if request.method == 'POST':
        query = request.POST['query'].strip()
        if query:
            # Run our Bing funciton to get the first 3 results!
            temp = run_query(query)
            for i in range(3):
                search_result.append(temp[i])


    context_dict = {}
    context_dict['boldmessage'] = 'Steam, Epic, Ubisoft, Origin, Battlenet!'
    context_dict['games'] = game_list1
    context_dict['hits'] = form_of_comments
    context_dict['search_result'] = search_result
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'gamehub/index.html', context=context_dict)


def about(request):
    context_dict = {'boldmessage': 'Team16'}
    return render(request, 'gamehub/about.html', context=context_dict)

def show_comments(request, game_name_slug):
    context_dict = {}
    try:
        game = Game.objects.get(slug=game_name_slug)
        comments = Comment.objects.filter(game=game)
        context_dict['comments'] = comments
        context_dict['game'] = game
    except Game.DoesNotExist:
        context_dict['game'] = None
        context_dict['comments'] = None
    return render(request, 'gamehub/comment.html', context=context_dict)




def view(request):
    obj = model_to_dict(Game.objects.get(id=request.GET.get("id")))
    comments = Comment.objects.filter(game_id=request.GET.get("id"))
    json_data = serializers.serialize('json', comments)
    json_data2 = json.loads(json_data)
    return render(request, 'gamehub/detail.html',{'context':obj,'comments':json_data2})

def queryByGameName(request):
    obj = Game.objects.all()
    json_data = serializers.serialize('json', obj)
    json_data2 = json.loads(json_data)
    return JsonResponse(json_data2,safe=False)

def sortByView(request):
    context_dict = {}
    list=Game.objects.order_by('-views')[:]
    context_dict = {'games': list,}
    return render(request, 'gamehub/sort.html', context=context_dict)

def sortByQual(request):
    context_dict = {}
    list=Game.objects.order_by('-avg_quality_rate')[:]
    context_dict = {'games': list,}
    return render(request, 'gamehub/sort.html', context=context_dict)

def sortByMusic(request):
    context_dict = {}
    list=Game.objects.order_by('-avg_music_rate')[:]
    context_dict = {'games': list,}
    return render(request, 'gamehub/sort.html', context=context_dict)

def sortByComm(request):
    context_dict = {}
    list=Game.objects.order_by('-avg_community_rate')[:]
    context_dict = {'games': list,}
    return render(request, 'gamehub/sort.html', context=context_dict)

def register(request):
    # A boolean value for telling the template
    # whether the registration was successful.
    # Set to False initially. Code changes value to
    # True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves,
            # we set commit=False. This delays saving the model
            # until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and
            # put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to indicate that the template
            # registration was successful.
            registered = True
        else:
            # Invalid form or forms - mistakes or something else?
            # Print problems to the terminal.
            print(user_form.errors, profile_form.errors)

    else:
        # Not a HTTP POST, so we render our form using two ModelForm instances.
        # These forms will be blank, ready for user input.
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request, 'gamehub/register.html', context = {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def user_login(request):
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        # We use request.POST.get('<variable>') as opposed
        # to request.POST['<variable>'], because the
        # request.POST.get('<variable>') returns None if the
        # value does not exist, while request.POST['<variable>']
        # will raise a KeyError exception.
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return redirect(reverse('gamehub:index'))
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Gamehub account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'gamehub/login.html')

@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return redirect(reverse('gamehub:index'))
