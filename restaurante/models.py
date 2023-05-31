from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.db import models

# Create your models here.

class RestauranteManager(BaseUserManager):
    def create_user(self, nombre, password, telefono, direccion, numero_pedido, **extra_fields):
        # Crea y guarda un nuevo usuario con contraseña hasheada
        if not nombre:
            raise ValueError('El nombre debe ser proporcionado')

        user = self.model(nombre=nombre, telefono=telefono, direccion=direccion, numero_pedido=numero_pedido, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nombre, password, telefono, direccion, numero_pedido, **extra_fields):
        # Crea y guarda un nuevo superusuario con contraseña hasheada
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(nombre, password, telefono, direccion, numero_pedido, **extra_fields)

class Restaurante(AbstractBaseUser):
    nombre = models.CharField(max_length=30, unique=True)
    telefono = models.PositiveIntegerField()
    especialidad = models.CharField(max_length=40, default="")
    # Otros campos requeridos por el modelo de usuario personalizado

    objects = RestauranteManager()

    USERNAME_FIELD = 'nombre'

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=50, null=False, default="")
    precio_fijo = models.IntegerField()
    imagen = models.ImageField(upload_to='photos', default="", null=True)
    disponibilidad = models.PositiveIntegerField(default=0,null=False)
    restaurante = models.ForeignKey(Restaurante,on_delete=models.CASCADE,null=False)
    def __str__(self):
        return f"{self.nombre_producto}: {self.precio_fijo}"

class Menu(models.Model):
    precio_variable = models.IntegerField(null=False, default=0)
    nombre_menu = models.CharField(max_length=50, null=False)
    descripcion = models.CharField(max_length=200, null=False)
    imagen = models.ImageField(upload_to='photos', default="", null=True)
    producto = models.ManyToManyField(Producto, blank=True,through='MenuProducto')
    disponibilidad = models.PositiveIntegerField(default=0, null=False)
    restaurante = models.ForeignKey(Restaurante,on_delete=models.CASCADE,null=False)

    def __str__(self):
        return f"{self.nombre_menu}: {self.precio_variable}"

class MenuProducto(models.Model):
    menu = models.ForeignKey(Menu,on_delete=models.CASCADE,null=True, blank=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True, blank=True)

