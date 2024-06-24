from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    preferencias = models.JSONField(default=dict, blank=True, null=True)


class Livro(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    ano_publicacao = models.IntegerField()

    def __str__(self):
        return self.titulo
