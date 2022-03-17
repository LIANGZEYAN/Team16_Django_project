import json

from django.core import serializers
from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from gamehub.models import Game
from gamehub.models import Comment

def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage matches to {{ boldmessage }} in the template!
    game_list = Game.objects.order_by('-views')[:3]
    context_dict = {}
    context_dict['boldmessage'] = 'Steam, Epic, Ubisoft, Origin, Battlenet!'
    context_dict['games'] = game_list
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