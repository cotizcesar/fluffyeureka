from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    ListView,
    FormView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.utils import timezone
from django.contrib import messages
from django.db.models import Count

#! Django: Importing User Model
from .models import User, UserProfile, Connection, Post, Game, Dodo

#! Core: Importing forms
from .forms import UserForm, UserProfileForm, UserProfileGameForm, PostForm, DodoForm


class Index(TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, *args, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context["games"] = Game.objects.all().order_by("title")[:10]
        context["users_date_joined"] = User.objects.all().order_by("-date_joined")[:10]
        context["users_last_login"] = User.objects.exclude(Q(userprofile__favorite_game__isnull=True) | Q(userprofile__nintendo_switch_code__isnull=True) | Q(userprofile__is_public=False)).order_by("-last_login")[:10]
        context["dodos"] = Dodo.objects.all()[:10]
        return context


class Feed(LoginRequiredMixin, ListView):
    model = Post
    paginate_by = 10
    template_name = "core/feed.html"

    def get_context_data(self, *args, **kwargs):
        context = super(Feed, self).get_context_data(**kwargs)
        context["object_list"] = Post.objects.filter(
            Q(user__in=self.request.user.follower.values("following"))
            | Q(user=self.request.user)
        ).order_by("-date_created")
        return context


class Members(ListView):
    model = User
    paginate_by = 10


class UserProfileDetailView(DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"
    context_object_name = "profile"

    def get_context_data(self, **kwargs):
        context = super(UserProfileDetailView, self).get_context_data(**kwargs)
        context["posts"] = Post.objects.filter(user=self.get_object()).order_by(
            "-date_created"
        )
        context["posts_count"] = Post.objects.filter(user=self.get_object()).count()

        #! Validation to show the Follow / Unfollow button.
        username = self.kwargs["username"]
        context["username"] = username
        context["user"] = self.request.user

        #! Following / Followers counters
        context["following_count"] = Connection.objects.filter(
            follower__username=username
        ).count()
        context["followers_count"] = Connection.objects.filter(
            following__username=username
        ).count()

        if username is not context["user"].username:
            result = Connection.objects.filter(
                follower__username=context["user"].username
            ).filter(following__username=username)
            context["connected"] = True if result else False
        return context


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = "core/userprofile_update.html"
    success_url = reverse_lazy("feed")

    def get_object(self):
        return self.request.user


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = "core/userprofile_update.html"
    success_url = reverse_lazy("feed")

    def form_valid(self, form):
        form.save(self.request.user)
        return super(UserProfileUpdateView, self).form_valid(form)

    def get_object(self):
        return self.request.user.userprofile

class UserProfileGameUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileGameForm
    template_name = "core/userprofile_update.html"
    success_url = reverse_lazy("feed")

    def form_valid(self, form):
        form.save(self.request.user)
        return super(UserProfileGameUpdateView, self).form_valid(form)

    def get_object(self):
        return self.request.user.userprofile


# Follow: hand-made system, its a better and modified copy
# https://github.com/benigls/instagram
@login_required
def follow_view(request, *args, **kwargs):
    try:
        follower = User.objects.get(username=request.user)
        following = User.objects.get(username=kwargs["username"])

    except User.DoesNotExist:
        messages.warning(
            request, "{} is not a registered user.".format(kwargs["username"])
        )
        return HttpResponseRedirect(reverse_lazy("feed"))

    if follower == following:
        messages.warning(request, "You cannot follow yourself.")

    else:
        _, created = Connection.objects.get_or_create(
            follower=follower, following=following
        )

        if created:
            messages.success(
                request, "You've successfully followed {}.".format(following.username)
            )

        else:
            messages.warning(
                request, "You've already followed {}.".format(following.username)
            )
    return HttpResponseRedirect(
        reverse_lazy("userprofile", kwargs={"username": following.username})
    )


# Unfollow: hand-made system, its a better and modified copy
# https://github.com/benigls/instagram
@login_required
def unfollow_view(request, *args, **kwargs):
    try:
        follower = User.objects.get(username=request.user)
        following = User.objects.get(username=kwargs["username"])

        if follower == following:
            messages.warning(request, "You cannot unfollow yourself.")

        else:
            unfollow = Connection.objects.get(follower=follower, following=following)
            unfollow.delete()
            messages.success(
                request, "You've just unfollowed {}.".format(following.username)
            )
    except User.DoesNotExist:
        messages.warning(
            request, "{} is not a registered user.".format(kwargs["username"])
        )
        return HttpResponseRedirect(reverse_lazy("feed"))

    except Connection.DoesNotExist:
        messages.warning(request, "You didn't follow {0}.".format(following.username))
    return HttpResponseRedirect(
        reverse_lazy("userprofile", kwargs={"username": following.username})
    )


class PostCreateView(LoginRequiredMixin, CreateView):
    form_class = PostForm
    template_name = "core/post_create.html"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.date_created = timezone.now()
        obj.save()
        return redirect("feed")


class DodoCreateView(LoginRequiredMixin, CreateView):
    form_class = DodoForm
    template_name = "core/dodo_create.html"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.date_created = timezone.now()
        obj.save()
        return redirect("feed")
