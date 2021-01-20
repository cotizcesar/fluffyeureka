from django import forms

#! Django: Importing User Model
from django.contrib.auth.models import User

#! Core: Models
from .models import UserProfile, Post, Dodo


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
        fields = ("header", "avatar", "biography")
        help_texts = {
            "header": "Only images in JPG and PNG are allowed.",
            "avatar": "Only images in JPG and PNG are allowed.",
            "biography": "Use this space for text, you have a limit of 160 characters.",
        }


class UserProfileGameForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("nintendo_switch_code", "favorite_game", "is_public")
        help_texts = {
            "favorite_game": "Select the game you like.",
            "is_public": "If you don't want to share your friend code publicly to unregistered users, uncheck this checkbox.",
            "nintendo_switch_code": "Add your friend code from your Nintendo Switch so that members can add you.",
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


class DodoForm(forms.ModelForm):
    class Meta:
        model = Dodo
        fields = (
            "text",
            "code",
            "image",
        )
