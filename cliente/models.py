from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.db import models


class ClienteManager(BaseUserManager):
    def create_user(self, nombre, password, telefono, direccion, numero_pedido, **extra_fields):
        # Crea y guarda un nuevo usuario con contraseña hasheada
        if not nombre:
            raise ValueError('El nombre debe ser proporcionado')

        user = self.model(nombre=nombre, telefono=telefono, direccion=direccion, numero_pedido=numero_pedido, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nombre, password, telefono, direccion, numero_pedido, **extra_fields):
        # Crea y guarda un nuevo superusuario con contraseña hasheada
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(nombre, password, telefono, direccion, numero_pedido, **extra_fields)

class Cliente(AbstractBaseUser):
    nombre = models.CharField(max_length=150, unique=True, null=False, default="")
    password = models.CharField(max_length=128)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)

    # Otros campos requeridos por el modelo de usuario personalizado

    objects = ClienteManager()

    USERNAME_FIELD = 'nombre'

class Pedido(models.Model):
    fecha = models.DateField()
    estado = models.CharField(max_length=30)
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE, null=False, default="0")
    pago = models.PositiveIntegerField(default=0,null=False)