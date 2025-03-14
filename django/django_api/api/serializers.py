from .models import Pokemon
from rest_framework import serializers

class pokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = '__all__'
