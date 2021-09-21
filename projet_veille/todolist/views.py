from todolist.models import Tache
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Tache
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

class ListeTache(ListView):
    model = Tache

class DetailTache(DetailView):
    model = Tache
    context_object_name = "tache"

class CreeTache(CreateView):
    model = Tache
    fields = '__all__' # tout les champs 
    success_url = reverse_lazy('taches') #retour à la page d'accueil
    