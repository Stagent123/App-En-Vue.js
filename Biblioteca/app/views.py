from app.models import Inventario,Libros,Prestamo,Genero,Libro_Genero
from app.serializers import InventarioSerializer,LibrosSerializer,PrestamoSerializer,GeneroSerializer,ListaGeneroSerializer
from django.shortcuts import render
from rest_framework import viewsets

class InventarioViewSet (viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer

class LibrosViewSet (viewsets.ModelViewSet):
    queryset = Libros.objects.all()
    serializer_class = LibrosSerializer

class PrestamoViewSet (viewsets.ModelViewSet):
    queryset= Prestamo.objects.all()
    serializer_class = PrestamoSerializer

class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

class LibroGeneroViewSet(viewsets.ModelViewSet):
    queryset = Libro_Genero.objects.all()
    serializer_class = Libro_Genero