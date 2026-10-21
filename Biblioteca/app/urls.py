from django.urls import path,include
from rest_framework.routers import DefaultRouter
from app.views import InventarioViewSet,LibrosViewSet,GeneroViewSet,LibroGeneroViewSet,PrestamoViewSet

router = DefaultRouter();
router.register(r'Inventario',InventarioViewSet,basename='inventario')
router.register(r'Libros',LibrosViewSet,basename='libro')
router.register(r'Prestamos',PrestamoViewSet,basename='prestamo')
router.register(r'Genero',GeneroViewSet,basename='genero')
router.register(r'LibroGenero',LibroGeneroViewSet,basename='librogenero')

UrlsBiblioteca = [
    path ('',include(router.urls))
]