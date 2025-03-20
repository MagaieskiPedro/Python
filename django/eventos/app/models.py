from django.db import models


# Create your models here.
class Eventos(models.Model):
    nome = models.CharField(max_length=25)
    descricao = models.TextField(max_length=100)
    data_hora = models.DateTimeField()
    local = models.CharField(max_length=25,null=True,blank=True)
    categoria = models.CharField(max_length=30,null=True,blank=True)
