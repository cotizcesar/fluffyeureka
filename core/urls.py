from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url

from .views import (
    Index,
    Feed,
    Members,
    UserProfileDetailView,
    UserUpdateView,
    UserProfileUpdateView,
    follow_view,
    unfollow_view,
    PostCreateView,
    DodoCreateView,
)

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("feed/", Feed.as_view(), name="feed"),
    path("members/", Members.as_view(), name="members"),
    url(
        r"^user/(?P<username>[a-zA-Z-_\d+\.]+)/$",
        UserProfileDetailView.as_view(),
        name="userprofile",
    ),
    url(r"^user/(?P<username>[a-zA-Z-_\d+\.]+)/follow/$", follow_view, name="follow"),
    url(
        r"^user/(?P<username>[a-zA-Z-_\d+\.]+)/unfollow/$",
        unfollow_view,
        name="unfollow",
    ),
    url(r"^accounts/basic/$", UserUpdateView.as_view(), name="userprofile_basic"),
    url(
        r"^accounts/advanced/$",
        UserProfileUpdateView.as_view(),
        name="userprofile_advanced",
    ),
    path("post/create/", PostCreateView.as_view(), name="post_create"),
    path("dodo/create/", DodoCreateView.as_view(), name="dodo_create"),
]
