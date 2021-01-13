from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url

from .views import Index, Members

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("members/", Members.as_view(), name="members"),
]