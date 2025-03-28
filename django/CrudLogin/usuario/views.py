from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

from .models import Usuario
from .serializer import UsuarioSerializer
# CADASTRO E LOGIN:
@api_view(['POST'])
def cadastro(request):
    nome = request.data.get("nome")
    senha = request.data.get("senha")
    biografia = request.data.get("biografia")
    idade = request.data.get("idade")
    telefone = request.data.get("telefone")
    endereco = request.data.get("endereco")
    escolaridade = request.data.get("escolaridade")
    num_animais = request.data.get("num_animais")
    if not nome or not senha:
        return Response({"error":"Nome e senha são obrigatorios"},status=status.HTTP_400_BAD_REQUEST)
    if Usuario.objects.filter(username=nome).exists():
        return Response({"error":"O usuario já existe"},status=status.HTTP_400_BAD_REQUEST)
    usuario = Usuario.objects.create_user(
        username=nome,
        password=senha,
        biografia=biografia,
        idade=idade,
        telefone=telefone,
        endereco=endereco,
        escolaridade=escolaridade,
        num_animais=num_animais
    )
    return Response({"mensagem":"Usuario criado com sucesso"},status=status.HTTP_201_CREATED)
@api_view(['POST'])
def login(request):
    nome = request.data.get("nome")
    senha = request.data.get("senha")
    usuario = authenticate(username=nome, password=senha)
    
    if usuario:
        refresh = RefreshToken.for_user(usuario)
        return Response({
            "Acesso":str(refresh.access_token),
            "Refresh":str(refresh)
            },status=status.HTTP_200_OK)
    else:
        return Response({"Erro":"usuario ou senha não encontrados"},status=status.HTTP_400_BAD_REQUEST)

# CRUD :
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def crud_read(request):
    usuario = Usuario.objects.all()
    serializer = UsuarioSerializer(usuario, many=True)
    return Response(serializer.data)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def crud_create(request):
    serializer = UsuarioSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def crud_update(request,pk):
    try:
        usuario = Usuario.objects.get(pk=pk)
    except Usuario.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    serializer = UsuarioSerializer(usuario, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def crud_delete(request,pk): 
    try:
        usuario = Usuario.objects.get(pk=pk)
    except Usuario.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    usuario.delete()
    return Response(status.HTTP_204_NO_CONTENT)