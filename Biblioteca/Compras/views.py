from django.shortcuts import render
from rest_framework import viewsets
from Compras.models import Transaccion,MetodoPago,Carrito,Objeto_Carrito
from Compras.serializers import MetodoPagoSerializer,CarritoSerializer,ObjetoCarritoSerializer,TransaccionSerializer

class MetodoPagoViewSet(viewsets.ModelViewSet):
    queryset = MetodoPago.objects.all()
    serializer_class = MetodoPagoSerializer

class TransaccionViewSet(viewsets.ModelViewSet):
    queryset = Transaccion.objects.all()
    serializer_class = TransaccionSerializer

class CarritoViewSet(viewsets.ModelViewSet):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer

class ObjectoCarritoViewSet(viewsets.ModelViewSet):
    queryset = Objeto_Carrito.objects.all()
    serializer_class = ObjetoCarritoSerializer
    

