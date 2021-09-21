import todolist
from todolist.models import Tache
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Tache
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView


class ListeTache(ListView):
    model = Tache


class DetailTache(DetailView):
    model = Tache
    context_object_name = "tache"


class CreeTache(CreateView):
    model = Tache
    fields = '__all__' # tout les champs 
    success_url = reverse_lazy('taches') #retour à la page d'accueil


class ModifierTache(UpdateView):
    model = Tache
    fields = '__all__'
    success_url = reverse_lazy('taches') 


class SupprTache(DeleteView):
    model = Tache
    success_url = reverse_lazy('taches') 


class LoginV(LoginView):
    template_name = "todolist/login.html"
    fields = '__all__'
    redirect_authenticated_user = True
    success_url = reverse_lazy('taches') 