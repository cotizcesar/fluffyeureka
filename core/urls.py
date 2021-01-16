from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url

from .views import Index, Members, UserProfileDetailView, follow_view, unfollow_view

urlpatterns = [
    path("", Index.as_view(), name="index"),
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
]
