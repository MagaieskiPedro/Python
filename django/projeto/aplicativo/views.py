from django.shortcuts import render
from django.http import HttpResponse
from .models import Postagem
# Create your views here.
def ola(request):
    return HttpResponse("Olá Mundo")
def ordenar_postagens(request):
    postagens = Postagem.objects.all().order_by('--dtCriacao')
    return render(request, 'blog/lista_postagens.html', {'postagens':postagens})