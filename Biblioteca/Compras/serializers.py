from rest_framework import serializers
from Compras.models import Compra,MetodoPago,Carrito,Transaccion,Objeto_Carrito

class TransaccionSerializer(serializers.ModelSerializer):
    class Meta:
        models = Transaccion
        fields = '__all__'

class MetodoPagoSerializer(serializers.ModelSerializer):
    class Meta:
        models = MetodoPago
        fields = '__all__'

class CarritoSerializer(serializers.ModelSerializer):
    class Meta: 
        models = Carrito
        fields = '__all__'

class ObjetoCarritoSerializer(serializers.ModelSerializer):
    class Meta:
        models = Objeto_Carrito
        fields = '__all__'

class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        models = Compra
        fields = '__all__'

# Completar con Tipos de metodo de pago luego
