import json

from django.core import serializers
from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from gamehub.bing_search import run_query
from gamehub.models import Game
from gamehub.models import Comment
from django.db.models import Count

def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage matches to {{ boldmessage }} in the template!
    game_list1 = Game.objects.order_by('-views')[:3]
    form_of_comments = Comment.objects.values('game__name', 'game__slug').annotate(num_of_comments = Count('game')).order_by()
    
    result = []
    for i in form_of_comments:  
        result.append(i['game__name'])

    # search
    search_result = []
    if request.method == 'POST':
        query = request.POST['query'].strip()
        if query:
            # Run our Bing funciton to get the results list!
            search_result = run_query(query)


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