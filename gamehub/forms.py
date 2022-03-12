from turtle import width
from django import forms
from django.contrib.auth.models import User
from gamehub import models
from gamehub.models import Comment

# We could add these forms to views.py, but it makes sense to split them off into their own file.

class CommentForm(forms.ModelForm):

    id = forms.IntegerField(widget=forms.HiddenInput)
    game = models.Game()
    content = forms.CharField(max_length=300)
    quality_rate = forms.IntegerField(default=0)
    music_rate = forms.IntegerField(default=0)
    community_rate = forms.IntegerField(default=0)

    class Meta:
        model = Comment
        fields = ('name',)