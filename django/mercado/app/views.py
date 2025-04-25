from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from rest_framework import serializers

from .models import Usuario, Produto
from .serializers import LoginSerializer, UsuarioSerializer, ProdutoSerializer
from .permissions import IsGestor,IsFuncionario,IsCliente,IsGestorOuFuncionario
# Create your views here.

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

class UsuarioListCreateAPIView(ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    perrmission_classes = [IsGestor]

class UsuarioRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    perrmission_classes = [IsGestor]
    lookup_field = 'pk'
    

class ProdutoListCreateAPIView(ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAuthenticated()]
        return [IsFuncionario()]