from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self,email,password=None, **extra_fields):
        if not email:
            raise ValueError("Email es requerido")
        email = self.normalize_email(email)
        user = self.model(email=email, password=password,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        return self.create_user(email,password,**extra_fields)

class Usuario(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    nombre =models.CharField(max_length=60)
    telefono = models.IntegerField( blank=True,  null=True, default=0)
    foto = models.FileField( blank=True, null=True)
    prestamos = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
