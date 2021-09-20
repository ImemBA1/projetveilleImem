from django.urls import path
from .views import DetailTache, ListeTache

urlpatterns = [
    path('', ListeTache.as_view(), name='tache'),
    path('tache/<int:pk>/', DetailTache.as_view(), name='tache'),
]