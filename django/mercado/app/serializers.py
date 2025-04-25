from rest_framework import serializers
from .models import Usuario,Produto
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
import pdb

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'
    def validate(self, attrs):
        data = super().validate(attrs)
        nome = data.get('nome')
        print(nome)
        if nome == 'Produto':
            data['nome'] = 'MudaNome'
        # if preco == 1:
        #     data['nome'] = 'Namae'
        return data
        # if data['nome'] == 'produto':
        #     self.Meta.model.quantidade = -3
        # if Produto.nome == 'produto':
        #     Produto.quantidade = -3
        # if data['nome'] == 'produto':
        #     data['quantidade'] = -3

class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['usuario'] = {
            'username': self.user.username,
            'categoria': self.user.categoria
        }
        # print(data['usuario'.])
        return data
