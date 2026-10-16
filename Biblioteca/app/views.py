from app.models import Inventario,Libros,Prestamo
from app.serializers import InventarioSerializer,LibrosSerializer,PrestamoSerializer
from django.shortcuts import render
from rest_framework import viewsets

class InventarioViewSet (viewsets.ViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer

class LibrosViewSet (viewsets.ViewSet):
    queryset = Libros.objects.all()
    serializer_class = LibrosSerializer

class PrestamoViewSet (viewsets.ViewSet):
    queryset= Prestamo.objects.all()
    serializer_class = PrestamoSerializer