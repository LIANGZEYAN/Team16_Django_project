from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to Gamehub! <a href='/gamehub/about/'>About</a>")

def about(request):
    return HttpResponse("This is about page!  <a href='/gamehub/'>Index</a>")