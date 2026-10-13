from django.db import models
from Usuarios.models import Usuario
from app.models import Libros
# Create your models here.

class MetodoPago(models.Model):
    ID = models.IntegerField(primary_key=True)
    Tipo = models.CharField()
    Nro_Tarjeta = models.IntegerField()

class Carrito(models.Model):
    ID = models.IntegerField(primary_key=True)
    ID_Usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
class Transaccion(models.Model):
    ID = models.IntegerField(primary_key=True)

class Objeto_Carrito(models.Model):
    ID_Carro = models.ForeignKey(Carrito,on_delete=models.CASCADE)
    ID_Libro = models.ForeignKey(Libros,on_delete=models.CASCADE)
    Cantidad = models.IntegerField()

class Compra(models.Model):
    Id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    ID_Carrito = models.ForeignKey(Carrito,on_delete=models.CASCADE)
    ID_Transacion = models.ForeignKey(Transaccion,on_delete=models.CASCADE)
    ID_MetodoPago = models.ForeignKey(MetodoPago,on_delete=models.CASCADE)
    Costo_Total = models.IntegerField()

