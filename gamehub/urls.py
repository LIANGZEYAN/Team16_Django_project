from django.urls import path
from gamehub import views

app_name = 'gamehub'

urlpatterns = [
path('', views.index, name='index'),
path('about/', views.about, name='about'),
]