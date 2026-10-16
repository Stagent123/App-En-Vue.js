from django.shortcuts import render
from rest_framework import viewsets
from Compras.models import Transaccion,MetodoPago,Carrito,Objeto_Carrito
from Compras.serializers import MetodoPagoSerializer,CarritoSerializer,ObjetoCarritoSerializer,TransaccionSerializer

class MetodoPagoViewSet(viewsets.ViewSet):
    queryset = MetodoPago.objects.all()
    serializer_class = MetodoPagoSerializer

class TransaccionViewSet(viewsets.ViewSet):
    queryset = Transaccion.objects.all()
    serializer_class = TransaccionSerializer

class CarritoViewSet(viewsets.ViewSet):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer

class ObjectoCarritoViewSet(viewsets.ViewSet):
    queryset = Objeto_Carrito.objects.all()
    serializer_class = ObjetoCarritoSerializer
    

    



# Create your views here.
