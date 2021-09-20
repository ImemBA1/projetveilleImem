from todolist.models import Tache
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Tache

class ListeTache(ListView):
    model = Tache

class DetailTache(DetailView):
    model = Tache
    context_object_name = "tache"