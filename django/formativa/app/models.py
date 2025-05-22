from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Professor(AbstractUser):
    CATEGORIA_ESCOLHA = [
        ('C','Comum'),
        ('G','Gestor')
    ]
    categoria = models.CharField(max_length=1,choices=CATEGORIA_ESCOLHA,default='C')
    ni = models.IntegerField()
    nome = models.CharField(max_length=15)
    telefone = models.IntegerField()
    data_nascimento = models.DateField()
    data_contratação = models.DateField()
    class Meta:
        verbose_name_plural = 'Professores'
    def __str__(self):
        return self.nome
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

    def __str__(self):
        return self.sala

class Disciplina(models.Model):
    nome = models.CharField(max_length=15)
    curso = models.CharField(max_length=15)
    carga_horaria = models.IntegerField()
    descrição = models.CharField(max_length=30)
    professor = models.ForeignKey(Professor,on_delete=models.CASCADE)
    ambiente = models.ForeignKey(Ambiente,on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


    
