from rest_framework import serializers
from .models import Eventos

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eventos
        fields = '__all__'