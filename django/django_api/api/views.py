from django.shortcuts import render
from .models import pokemon
from rest_framework.response import Response

# Create your views here.
def read_pokemon():
    pokemons = pokemon.objects.all()
    serializer = pokemonSerializer(pokemons, many=True)
    return Response(serializer.data)