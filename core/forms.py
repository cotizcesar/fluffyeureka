from django import forms

#! Django: Importing User Model
from django.contrib.auth.models import User

#! Core: Models
from .models import UserProfile, Post

from allauth.account.forms import SignupForm

from .validators import username_validator


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name")
        help_texts = {
            "first_name": "If you want to use your first name you can place it here.",
            "last_name": "If you use your first name, you should also put your last name, so its easier to know what your name really is.",
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("avatar", "biography")
        help_texts = {
            "avatar": "Only images in JPG and PNG are allowed.",
            "biography": "Use this space for text, you have a limit of 160 characters.",
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("text", "image", "video")
        help_texts = {
            "text": "Use this space for text, you have a limit of 280 characters.",
            "image": "Only images in JPG and PNG are allowed.",
            "video": "Copy and paste an URL from the following sites: YouTube.com, Twitch.tv, Vimeo.com or Giphy.com.",
        }
