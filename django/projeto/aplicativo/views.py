from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def ola(request):
    return HttpResponse("Olá Mundo")
