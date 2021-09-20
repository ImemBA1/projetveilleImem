from todolist.models import Tache
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Tache

class ListeTache(ListView):
    model = Tache
