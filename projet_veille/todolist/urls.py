from django.urls import path
from .views import CreeTache, DetailTache, ListeTache, ModifierTache

urlpatterns = [
    path('', ListeTache.as_view(), name='taches'),
    path('tache/<int:pk>/', DetailTache.as_view(), name='tache'),
    path('cree-tache/', CreeTache.as_view(), name='cree-tache'),
    path('modif-tache/<int:pk>/', ModifierTache.as_view(), name='modif-tache')
]