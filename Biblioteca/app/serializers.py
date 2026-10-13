from rest_framework import serializers
from app.models import Libros, Inventario,Prestamo,

class LibrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libros
        fields = '__all__'

class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = '__all__'

class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = '__all__'
    