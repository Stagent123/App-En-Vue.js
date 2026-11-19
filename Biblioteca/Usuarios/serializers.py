from rest_framework import serializers
from Usuarios.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    foto = serializers.ImageField(read_only=True)

    class Meta:
        model = Usuario
        fields = '__all__'


