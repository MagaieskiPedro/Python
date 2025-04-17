from django.shortcuts import render
from rest_framework import serializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
import re
from datetime import datetime, date
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Aniversariante
from .serializers import AniversarianteSerializer , LoginSerializer
# ObterTokenSerializer


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
        CPFregex = '^\\d{3}.\\d{3}.\\d{3}-\\d{2}$'
        cpf = serializer.validated_data['cpf']
        data = serializer.validated_data['data']
        idade = serializer.validated_data['idade']

        # Aqui fazer validação comparando data atual com a data de nascimento e ver se é igual a idade
        # data_agora = date.today()
        # if data_agora - data != idade:
        #     raise serializers.ValidationError(f"Idade não bate com a data de nascimento")
        
        if not re.match(CPFregex,cpf):
            raise serializers.ValidationError("Cpf deve ser no formato adequado")
        serializer.save()

class AniversarianteRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Aniversariante.objects.all()
    serializer_class = AniversarianteSerializer
    lookup_field = 'pk'

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer