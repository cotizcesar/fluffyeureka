from django.db import models

#! Django: Importing User Model
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

#! Core: UserProfile reciever and post_save signal: Needed to create a UserProfile objects when the User account its created.
from django.dispatch import receiver
from django.db.models.signals import post_save

#! django-autoslug: Added custom Field.
# https://django-autoslug.readthedocs.io/en/latest/#examples
from autoslug import AutoSlugField


class Game(models.Model):
    title = models.CharField(max_length=140)
    slug = AutoSlugField(populate_from="title", unique=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    header = models.ImageField(
        upload_to="user/header", default="user/header/default.png", blank=True
    )
    avatar = models.ImageField(
        upload_to="user/avatar", default="user/avatar/default.png", blank=True
    )
    biography = models.TextField(max_length=160, blank=True)
    nintendo_switch_code = models.PositiveBigIntegerField(
        validators=[MinValueValidator(000000000000), MaxValueValidator(999999999999)],
        blank=True,
        null=True,
    )
    game = models.OneToOneField(Game, on_delete=models.PROTECT, blank=True, null=True)
    is_public = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


class Connection(models.Model):
    follower = models.ForeignKey(
        User, related_name="follower", on_delete=models.PROTECT
    )
    following = models.ForeignKey(
        User, related_name="following", on_delete=models.PROTECT
    )
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} : {}".format(self.follower.username, self.following.username)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=280)
    image = models.ImageField(upload_to="user/post", blank=True)
    video = models.URLField(blank=True)
    comment = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        default=None,
        blank=True,
        null=True,
        related_name="comments",
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_pinned = models.BooleanField(default=False)


class Dodo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=280)
    code = models.CharField(max_length=5)
    image = models.ImageField(upload_to="user/dodo", blank=True)
    video = models.URLField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_pinned = models.BooleanField(default=False)
