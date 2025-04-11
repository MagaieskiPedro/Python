from django.shortcuts import render
from rest_framework import serializers
from rest_framework.generics import ListCreateAPIView
from .models import Aniversariante
from .serializers import AniversarianteSerializer
from rest_framework.pagination import PageNumberPagination
import re
# Create your views here.
class AniversariantePaginacao(PageNumberPagination):
    page_size = 5
    max_page_size = 20
    page_number = 10
    page_size_query_param = 'page_size'

class AniversarianteListCreateAPIView(ListCreateAPIView):
    queryset = Aniversariante.objects.all()
    serializer_class = AniversarianteSerializer
    pagination_class = AniversariantePaginacao

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.query_params.get('nome')
        if nome:
            queryset = queryset.filter(nome__icontains = nome)
        return queryset
    def perform_create(self, serializer):
        regex = '^\d{3}.\d{3}.\d{3}-\d{2}$'
        cpf = serializer.validated_data['cpf']
        if not re.match(regex,cpf):
            raise serializers.ValidationError("Cpf deve ser no formato adequado")
        serializer.save()