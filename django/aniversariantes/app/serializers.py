from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Aniversariante, Usuario
class AniversarianteSerializer(serializers.ModelSerializer):
    class Meta:
        model= Aniversariante
        fields= "__all__"
        read_only_fields = ['id']
# class ObterTokenSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField(write_only=True)

#     def validate(self, attrs):
#         username = attrs.get('username')
#         password = attrs.get('password')

#         if username and password:
#             usuario = authenticate(request=self.context.get('request'),
#                                    username=username,
#                                    password=password)
#             if not usuario:
#                 raise serializers.ValidationError('Usuaraio ou senha invalidos', code='authorization')
#         else:
#             raise serializers.ValidationError('usuario e senha são obrigatorios', code='authorization')
#         attrs['usuario'] = UsuarioSerializer(usuario).data
#         return attrs
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields ='__all__'

class LoginSerializer(TokenObtainPairSerializer):
    def validate(self,attrs):
        data = super().validate(attrs)

        data['usuario'] = {
            'username': self.user.username,
            'email': self.user.email,
            'foto': self.user.foto_perfil
        }

        return data