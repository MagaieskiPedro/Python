from django.db import models

# Create your models here.
class pokemon(models.Model):
    nome = models.CharField(max_length=20)
    geracao = models.PositiveIntegerField()
    tipo = models.CharField(max_length=20)
    habilidade = models.TextField()

    def __str__(self):
        return self.nome

