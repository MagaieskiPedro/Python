from django.shortcuts import render
from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Professor,Ambiente,Disciplina,Usuario
from .serializer import ProfessorSerializer,AmbienteSerializer,DisciplinaSerializer,LoginSerializer
from .permissions import isGestor
# Create your views here.
class ProfessorView(viewsets.ViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    permission_classes = [isGestor]
    lookup_field = 'pk'
class AmbienteView(viewsets.ViewSet):
    queryset = Ambiente.objects.all()
    serializer_class = AmbienteSerializer
    permission_classes = [isGestor]
    lookup_field = 'pk'
class DisciplinaView(viewsets.ViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    permission_classes = [isGestor]
    lookup_field = 'pk'
class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer