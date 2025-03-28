from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Usuario(AbstractUser):
    biografia = models.TextField(blank=True, null=True)
    idade = models.IntegerField(blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    endereco = models.CharField(max_length=25, blank=True, null=True)
    escolaridade = models.CharField(max_length=15, blank=True, null=True)
    num_animais = models.IntegerField(blank=True, null=True)
