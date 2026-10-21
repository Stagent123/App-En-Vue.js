from django.contrib import admin
from app.models import Genero,Libro_Genero,Libros,Inventario,Prestamo

admin.site.register(Inventario)
admin.site.register(Libros)
admin.site.register(Genero)
admin.site.register(Libro_Genero)
admin.site.register(Prestamo)
# Register your models here.
