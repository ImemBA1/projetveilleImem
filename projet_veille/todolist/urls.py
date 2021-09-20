from django.urls import path
from .views import ListeTache

urlpatterns = [
    path('', ListeTache.as_view(), name='tache'),
]