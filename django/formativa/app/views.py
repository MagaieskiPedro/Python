from django.shortcuts import render
from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.generics import ListAPIView

from .models import Professor,Ambiente,Disciplina
from .serializer import ProfessorSerializer,AmbienteSerializer,DisciplinaSerializer,LoginSerializer,CadastroSerializer
from .permissions import isGestor,isComum
# Create your views here.
class ProfessorView(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    permission_classes = [isGestor]
    lookup_field = 'pk'
class AmbienteView(viewsets.ModelViewSet):
    queryset = Ambiente.objects.all()
    serializer_class = AmbienteSerializer
    permission_classes = [isGestor]
    lookup_field = 'pk'
class DisciplinaView(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    permission_classes = [isGestor]
    lookup_field = 'pk'
class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

class CadastroView(generics.CreateAPIView):
    queryset = Professor.objects.all()
    serializer_class = CadastroSerializer
