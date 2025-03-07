from django.db import models

# Create your models here.
class Livro(models.Model):
    titulo = models.CharField(max_length=10)
    autor = models.CharField(max_length=10)
    anoPub = models.DateField()
    
    def __str__(self):
        return self.titulo
    class Meta:
        verbose_name_plural = 'Livros'