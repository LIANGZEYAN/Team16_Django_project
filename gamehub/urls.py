from django.urls import path
from gamehub import views


app_name = 'gamehub'

urlpatterns = [
path('', views.index, name='index'),
path('about/', views.about, name='about'),
path('comment/<slug:game_name_slug>/', views.show_comments, name='show_comments'),
path('comment/<slug:game_name_slug>/rate/', views.rate, name='rate'),
path('view/', views.view,name='id'),
path('queryByGameName/', views.queryByGameName),
path('sort/', views.sortByView, name='sortByView'),
path('sort/quality', views.sortByQual, name='sortByQual'),
path('sort/music', views.sortByMusic, name='sortByMusic'),
path('sort/community', views.sortByComm, name='sortByComm'),
path('register/', views.register, name='register'),
path('login/', views.user_login, name='login'),
path('restricted/', views.restricted, name='restricted'),
path('logout/', views.user_logout, name='logout'),
path('thanks/', views.thanks, name='thanks'),
]