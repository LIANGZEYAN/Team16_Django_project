from django.urls import path
from gamehub import views


app_name = 'gamehub'

urlpatterns = [
path('', views.index, name='index'),
path('about/', views.about, name='about'),
path('comment/<slug:game_name_slug>/', views.show_comments, name='show_comments'),
path('rate/', views.rate, name='rate'),
path('view/', views.view,name='id'),
path('queryByGameName/', views.queryByGameName),

]