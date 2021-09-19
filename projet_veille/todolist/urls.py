from django.urls import path
from . import views

urlpatterns = [
    path('', views.listeTache, name='tache'),
]