from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', ListeTache.as_view(), name='taches'),
    path('tache/<int:pk>/', DetailTache.as_view(), name='tache'),
    path('cree-tache/', CreeTache.as_view(), name='cree-tache'),
    path('modif-tache/<int:pk>/', ModifierTache.as_view(), name='modif-tache'),
    path('suppr-tache/<int:pk>/', SupprTache.as_view(), name='suppr-tache'),
    path('login/', LoginV.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterV.as_view(), name='register')

]