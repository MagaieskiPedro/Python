from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view 
from rest_framework import status

from .models import Pokemon
from .serializers import pokemonSerializer

# Create your views here.
@api_view(['GET'])
def read_pokemons(request):
    pokemons = Pokemon.objects.all()
    serializer = pokemonSerializer(pokemons, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def read_pokemon(request,pk):
    try:
        pokemon = Pokemon.objects.get(pk=pk)
    except Pokemon.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    serializer = pokemonSerializer(pokemon)
    return Response(serializer.data)

@api_view(['POST'])
def create_pokemon(request):
    serializer = pokemonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_pokemon(request, pk):
    try:
        pokemon = Pokemon.objects.get(pk=pk)
    except Pokemon.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    serializer = pokemonSerializer(pokemon, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_pokemon(request, pk):
    try:
        pokemon = Pokemon.objects.get(pk=pk)
    except Pokemon.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    pokemon.delete()
    return Response(status.HTTP_204_NO_CONTENT)
@api_view(['PATCH'])
def update_parcial_pokemon(request, pk):
    try:
        pokemon = Pokemon.objects.get(pk=pk)
    except Pokemon.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    serializer = pokemonSerializer(pokemon, data = request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
