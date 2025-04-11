from rest_framework import serializers
from .models import Aniversariante
class AniversarianteSerializer(serializers.ModelSerializer):
    class Meta:
        model= Aniversariante
        fields= "__all__"
        read_only_fields = ['id']