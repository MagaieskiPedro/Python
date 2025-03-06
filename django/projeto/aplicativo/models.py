from django.db import models

# Create your models here.
class Postagem(models.Model):
    titulo = models.CharField(max_length=20)
    conteudo = models.TextField()
    dtCriacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    class Meta:
        verbose_name_plural = "Postagens"