from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    CATEGORIA_ESCOLHA = [
        ('C','Cliente'),
        ('F','Funcionario'),
        ('G','Gestor')
    ]
    categoria = models.CharField(max_length=1,choices=CATEGORIA_ESCOLHA,default='C')
    def __str__(self):
        return self.username
class Produto(models.Model):
    nome = models.CharField(max_length=15)
    codigo = models.CharField(max_length=20)
    preco = models.FloatField()
    quantidade = models.IntegerField()
    dt_vencimento = models.DateField()

    def __str__(self):
        return self.nome
    
    