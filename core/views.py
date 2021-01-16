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
from .models import User, UserProfile, Connection, Post

#! Core: Importing forms
from .forms import PostForm


class Index(TemplateView):
    template_name = "core/index.html"


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
        return redirect("index")
