from django import forms
from django.contrib.auth.models import User
from gamehub.models import UserProfile
from gamehub import models
from gamehub.models import Comment

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture',)



# We could add these forms to views.py, but it makes sense to split them off into their own file.

class CommentForm(forms.ModelForm):

    
    #game = models.Game()
    #id = forms.IntegerField(widget=forms.NumberInput)
    content = forms.CharField(max_length=300)
    quality_rate = forms.IntegerField(widget=forms.NumberInput,max_value=5, initial=0)
    music_rate = forms.IntegerField(widget=forms.NumberInput,max_value=5, initial=0)
    community_rate = forms.IntegerField(widget=forms.NumberInput,max_value=5, initial=0)

    class Meta:
        model = Comment
        #exclude = ('game',)
        fields = ('content','quality_rate','music_rate','community_rate',)
        

    
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        #self.fields['music_rate'].widget.attrs['size'] = 20
        self.fields['music_rate'].widget.attrs['class'] = 'number-input'
        self.fields['quality_rate'].widget.attrs['class'] = 'number-input'
        self.fields['community_rate'].widget.attrs['class'] = 'number-input'
        self.fields['content'].widget.attrs['class'] = 'txt-input'
