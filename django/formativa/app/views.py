from django.shortcuts import render
from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics


from .models import Professor,Ambiente,Disciplina
from .serializer import ProfessorSerializer,AmbienteSerializer,DisciplinaSerializer,LoginSerializer,CadastroSerializer, reservasProfessorSerializer
from .permissions import isGestor,isComum, isAuthenticated
# Create your views here.
class ProfessorView(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    permission_classes = [isGestor]
    lookup_field = 'pk'
class AmbienteView(viewsets.ModelViewSet):
    queryset = Ambiente.objects.all()
    serializer_class = AmbienteSerializer
    def get_permissions(self):
        if self.request.method == 'POST':
            return [isGestor()]
        return [isAuthenticated()]
    def get_queryset(self):
        user = self.request.user
        if user.categoria == 'C':
            return Ambiente.objects.filter(professor=user)
        elif user.categoria == 'G':
            return Ambiente.objects.all()
        else:
            return Ambiente.objects.none()
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
class reservasProfessores(generics.ListAPIView):
    queryset = Ambiente.objects.all()
    # Criar serilizador que filtra apenas ambientes do professor logado
    #serializer_class = AmbienteSerializer
    permission_classes = [isGestor]
class disciplinaProfessores(generics.ListAPIView):
    queryset = Disciplina.objects.all()
    # Criar serilizador que filtra apenas disciplinas do professor logado
    serializer_class = reservasProfessorSerializer
    permission_classes = [isGestor,isComum]