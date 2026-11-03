from app.models import Inventario,Libros,Prestamo,Genero,Libro_Genero
from app.serializers import InventarioSerializer,LibrosSerializer,PrestamoSerializer,GeneroSerializer,ListaGeneroSerializer
from django.shortcuts import render
from rest_framework import viewsets
from Usuarios.permissions import InventarioPermission, permissions

class InventarioViewSet (viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer
    permission_classes = [permissions.IsAuthenticated, InventarioPermission]

class LibrosViewSet (viewsets.ModelViewSet):
    queryset = Libros.objects.all()
    serializer_class = LibrosSerializer
    permission_classes = [permissions.IsAuthenticated, InventarioPermission]

class PrestamoViewSet (viewsets.ModelViewSet):
    queryset= Prestamo.objects.all()
    serializer_class = PrestamoSerializer
    permission_classes = [permissions.IsAuthenticated, InventarioPermission]

class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer
    permission_classes = [permissions.IsAuthenticated, InventarioPermission]

class LibroGeneroViewSet(viewsets.ModelViewSet):
    queryset = Libro_Genero.objects.all()
    serializer_class = Libro_Genero
    permission_classes = [permissions.IsAuthenticated, InventarioPermission]