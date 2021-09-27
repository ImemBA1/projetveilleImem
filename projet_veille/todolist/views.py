import todolist
from todolist.models import Tache
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Tache
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin


class ListeTache(LoginRequiredMixin, ListView):
    model = Tache
    context_object_name = "taches"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['taches'] = context['taches'].filter(utilisateur=self.request.user)
        context['count'] = context['taches'].filter(termine=False).count()
        return context


class DetailTache(LoginRequiredMixin, DetailView):
    model = Tache
    context_object_name = "tache"


class CreeTache(LoginRequiredMixin, CreateView):
    model = Tache
    fields = '__all__' # tout les champs 
    success_url = reverse_lazy('taches') #retour à la page d'accueil


class ModifierTache(LoginRequiredMixin, UpdateView):
    model = Tache
    fields = '__all__'
    success_url = reverse_lazy('taches') 


class SupprTache(LoginRequiredMixin, DeleteView):
    model = Tache
    success_url = reverse_lazy('taches') 


class LoginV(LoginView):
    template_name = "todolist/login.html"
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('taches')