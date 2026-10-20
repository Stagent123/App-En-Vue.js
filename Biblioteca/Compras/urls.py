from django.urls import path,include
from rest_framework.routers import DefaultRouter
from Compras.views import CarritoViewSet,MetodoPagoViewSet,TransaccionViewSet,ObjectoCarritoViewSet


router = DefaultRouter();
router.register(r'Carrito',CarritoViewSet,basename='carrito')
router.register(r'MetodoPago',MetodoPagoViewSet,basename='metodopago')
router.register(r'Transaccion',TransaccionViewSet,basename='transaccion')
router.register(r'ObjetoCarrito',ObjectoCarritoViewSet,basename='objcarrito')


UrlsCompras = [
    path('',include(router.urls))
]
