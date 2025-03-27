from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Usuario

# Create your views here.
@api_view(['POST'])
def registrar(request):
    nome = request.data.get('nome')
    senha = request.data.get('senha')
    telefone = request.data.get('telefone')
    endereco = request.data.get('endereco')
    cpf = request.data.get('cpf')
    email = request.data.get('email')

    if not nome or not senha or not cpf or not email:
        return Response({'erro':'Os campos nome,senha,cpf,email sao obrigatorios'},status=status.HTTP_400_BAD_REQUEST)
    if Usuario.objects.filter(username=nome).exists():
        return Response({'erro':'Usuario já existe'},status=status.HTTP_400_BAD_REQUEST)
    usuario = Usuario.objects.create_user(
        username=nome,
        password=senha,
        telefone=telefone,
        email=email,
        cpf=cpf,
        endereco=endereco
    )

    return Response({'mensagem':'Usuario cadastrado com sucesso'}, status=status.HTTP_201_CREATED)

    