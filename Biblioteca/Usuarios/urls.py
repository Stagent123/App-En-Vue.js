from django.urls import path,include
from rest_framework.routers import DefaultRouter
from Usuarios.views import UsuarioViewSet,LoginView,LogoutView,CurrentUserView

router = DefaultRouter();
router.register(r'Usuario',UsuarioViewSet,basename='usuario')


UrlsUsuario = [
    path('Login',LoginView.as_view(),name='login'),
    path('Logout',LogoutView.as_view(),name='logout'),
    path('Auth',CurrentUserView.as_view(),name='auth'),
    path('',include(router.urls))
]
