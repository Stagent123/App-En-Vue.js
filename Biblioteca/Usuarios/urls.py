from django.urls import path,include
from rest_framework.routers import DefaultRouter
from Usuarios.views import UsuarioViewSet

router = DefaultRouter();
router.register(r'Usuario',UsuarioViewSet,basename='usuario')

UrlsUsuario = [
    path('',include(router.urls))
]
