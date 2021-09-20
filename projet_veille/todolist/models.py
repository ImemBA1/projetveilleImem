from django.db import models
from django.contrib.auth.models import User


class Tache(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titre = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    termine = models.BooleanField(default=False)
    cree = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

    class Meta:
        ordering = ['termine']

