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
from django.contrib.auth.models import User


class Index(TemplateView):
    template_name = "core/index.html"


class Members(ListView):
    model = User
    paginate_by = 21
