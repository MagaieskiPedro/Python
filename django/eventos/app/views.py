from django.shortcuts import render
from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from rest_framework import status


from .models import Eventos
from .serializer import EventoSerializer
# Create your views here.
        
@api_view(['GET'])
def read_eventos(request):
    categoria = request.query_params.get('categoria')
    data = request.query_params.get('data_hora')
    quantidade = request.query_params.get('quantidade') 
    page = request.query_params.get('page') 
    eventos =  Eventos.objects.all() 
    if quantidade and page:
        paginator = Paginator(eventos,quantidade)
        eventos = paginator.page(page)
    if categoria:
        eventos = eventos.filter(categoria__icontains=categoria)
    if data:
        eventos = eventos.filter(data_hora__icontains=data)
    serializer = EventoSerializer(eventos, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def read_evento(request,pk):
    try:
        evento = Eventos.objects.get(pk=pk)
    except:
        return Response(status.HTTP_404_NOT_FOUND)
    serializer = EventoSerializer(evento)
    return Response(serializer.data)
@api_view(['POST'])
def create_evento(request):
    serializer = EventoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status.HTTP_201_CREATED)
    return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
@api_view(['PUT'])
def update_evento(request,pk):
    try:
        evento = Eventos.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = EventoSerializer(evento,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status.HTTP_202_ACCEPTED)
    return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
def delete_evento(request,pk):
    try:
        evento = Eventos.objects.get(pk=pk)
    except Eventos.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    evento.delete()
    return Response(status.HTTP_204_NO_CONTENT)
@api_view(['PATCH'])
def update_partial_evento(request,pk):
    try:
        evento = Eventos.objects.get(pk=pk)
    except Eventos.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    serializer = EventoSerializer(evento, data= request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(status.HTTP_202_ACCEPTED)
    return Response(status.HTTP_400_BAD_REQUEST)
