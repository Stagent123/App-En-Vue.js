from django.db import models
from django.contrib.auth.models import BaseUserManager, PermissionsMixin




class CustomUserManager(BaseUserManager):
    def create_user(selfm email,username, Password,** extra_fields):
        if not email:
            raise ValueError("El campo de email debe contener un email")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.save(using=self.db)
        return user
    def create_superuser (self, email , username, Password, **extra_fields):
        extra_fields.setdefault("is_staff,True")
        extra_fields.setdefault("is_superuser",True)
        extra_fields.setdefault("is_active",True)
        return self.create_user(email,username, **extra_fields)

class CustomUser(models.Model, PermissionsMixin):
    email= models.EmailField(unique=True)
    username= models.CharField()
    is_active = models.BooleanField()
    is_staff = models.BooleanField()
    date_joined = models.DateTimeField(auto_now_add=True)
    objets = CustomUserManager()

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELD = ["username", "password"]

    def __str__(self):
        return self.email

class Usuario(models.Model):
    ID = models.IntegerField(primary_key=True)
    Nombre = models.CharField
    password = models.passwordField