from django.shortcuts import render
from rest_framework import viewsets
from Usuarios.models import Usuario
from Usuarios.serializers import UsuarioSerializer
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from rest_framework.views import APIView
from rest_framework import status


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset= Usuario.objects.all()
    serializer_class = UsuarioSerializer

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self,request):
        username = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request,username=username,password=password)
        if user is None:
            login(request,user)
            return Response({"message": 'Login Successful'}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credencials"}, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    permission_classes = [permission.isAuthenticated]

    def post(self,request):
        logout(request)
        return Response({"message" : "Logged out successfully"}, status=status.HTTP_200_OK)

# Create your views here.
