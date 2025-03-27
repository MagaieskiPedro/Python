from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    telefone = models.CharField(max_length=15, blank=True, null=True)
    cpf = models.CharField(max_length=20,blank=True,null=True)
    endereco = models.CharField(max_length=20,blank=True,null=True)


