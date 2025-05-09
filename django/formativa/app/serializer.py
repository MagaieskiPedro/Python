from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Professor,Ambiente,Disciplina

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'
class AmbienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ambiente
        fields = '__all__'
class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = '__all__'

class LoginSerializer(TokenObtainPairSerializer):
    def validate(self,attrs):
        data = super().validate(attrs)
        data['professor'] = {
            'username': self.user.username,
            'categoria': self.user.categoria
        }
        return data
class CadastroSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Professor
        fields = ('ni','nome','telefone','data_nascimento','data_contratação','password','password2','categoria')
    
    def validate(self, attrs):
        data = super().validate(attrs)
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password":"Campos senha não bateram"}
            )
        return attrs
    def create(self, validated_data):
        
        validated_data['username'] = validated_data['nome']
        
        user = Professor.objects.create(
            ni= validated_data['ni'],
            username=validated_data['nome'],
            nome=validated_data['nome'],
            telefone=validated_data['telefone'],
            data_nascimento=validated_data['data_nascimento'],
            data_contratação=validated_data['data_contratação'],
            categoria=validated_data['categoria'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user



