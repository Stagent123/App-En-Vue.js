from rest_framework import serializers
from app.models import Libros, Inventario,Prestamo,Genero,Libro_Genero

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

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model= Genero
        fields = '__all__'

class ListaGeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model= Libro_Genero
        fields = '__all__'
    