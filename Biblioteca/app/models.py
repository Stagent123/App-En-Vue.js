from django.db import models
from Usuarios.models import Usuario

# Create your models here.


class Libros(models.Model):
    ID = models.IntegerField(primary_key=True)
    Generos = models.CharField()
    Editorial = models.CharField()
    Version = models.CharField()
    Autor = models.CharField()
    Paginas = models.IntegerField()
    Titulo = models.CharField()
    Portada = models.ImageField()
    Sinopsis = models.TextField()


class Inventario(models.Model):
    ID_Libro = models.ForeignKey(Libros, on_delete=models.CASCADE)
    Valor = models.IntegerField()
    Disponible_Venta = models.BooleanField()
    Disponible_Compra= models.BooleanField()



class Prestamo(models.Model):
    Id = models.IntegerField(primary_key=True)
    ID_Libro = models.ForeignKey(Libros, on_delete=models.CASCADE)
    ID_Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    Fecha_Inicial = models.DateField()
    Fecha_Regreso = models.DateField()
    Fecha_Maxima = models.DateField()
    Regresado = models.BooleanField()

