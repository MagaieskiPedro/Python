from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Professor(AbstractUser):
    CATEGORIA_ESCOLHA = [
        ('C','Comum'),
        ('G','Gestor')
    ]
    categoria = models.CharField(max_length=1,choices=CATEGORIA_ESCOLHA,default='C')
    ni = models.IntegerField(default=1)
    nome = models.CharField(max_length=15)
    telefone = models.IntegerField(default=1)
    data_nascimento = models.DateField(default="2000-1-1")
    data_contratação = models.DateField(default="2000-1-1")
    class Meta:
        verbose_name_plural = 'Professores'
class Ambiente(models.Model):
    PERIODO = [
        ('M','Manhã'),
        ('T','Tarde'),
        ('N','Noite')
    ]
    data_inicio = models.DateField()
    data_termino = models.DateField()
    periodo = models.CharField(choices=PERIODO, default='M',max_length=1)
    sala = models.CharField(max_length=15)
    
    professor = models.ForeignKey(Professor,on_delete=models.CASCADE)

class Disciplina(models.Model):
    nome = models.CharField(max_length=15)
    curso = models.CharField(max_length=15)
    carga_horaria = models.IntegerField()
    descrição = models.CharField(max_length=30)
    professor = models.ForeignKey(Professor,on_delete=models.CASCADE)
    ambiente = models.ForeignKey(Ambiente,on_delete=models.CASCADE)


    
