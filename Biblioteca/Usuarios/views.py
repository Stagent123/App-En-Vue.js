from django.shortcuts import render
from rest_framework import viewsets
from Usuarios.models import Usuario
from Usuarios.serializers import UsuarioSerializer
# Create your views here.

class UsuarioSerializer(viewsets.ViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer