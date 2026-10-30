from django.urls import path,include
from rest_framework.routers import DefaultRouter
from Usuarios.views import UsuarioViewSet,LoginView,LogoutView,CurrentUserView

router = DefaultRouter();
router.register(r'Usuario',UsuarioViewSet,basename='usuario')
router.register(r'Login',LoginView,basename='login')
router.register(r'Logout',LogoutView,basename='logout')
router.register(r'Auth',CurrentUserView,basename='auth')

UrlsUsuario = [
    path('',include(router.urls))
]
