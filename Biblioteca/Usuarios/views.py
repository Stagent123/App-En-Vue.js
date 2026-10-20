from django.shortcuts import render
from rest_framework import viewsets
from Usuarios.models import Usuario
from Usuarios.serializers import UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset= Usuario.objects.all()
    serializer_class = UsuarioSerializer