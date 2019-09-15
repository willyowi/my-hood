from django import forms
from .models import Profile 
# Business, NeighbourHood, Post, Comment

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

# class BusinessForm(forms.ModelForm):
#     class Meta:
#         model = Business
#         exclude = ['user', 'neighbourhood']

# class NeighbourHoodForm(forms.ModelForm):
#     class Meta:
#         model = NeighbourHood
#         fields = ('name', 'location', 'occupants')

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         exclude = ['user', 'neighbourhood']

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('comment',)