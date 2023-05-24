from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre_producto = models.CharField(max_length=50, null=False, default="")
    precio_fijo = models.IntegerField()
    imagen = models.ImageField(upload_to='photos', default="", null=True)
    def __str__(self):
        return f"{self.nombre_producto}: {self.precio_fijo}"

class Menu(models.Model):
    precio_variable = models.IntegerField(null=False)
    nombre_menu = models.CharField(max_length=50, null=False)
    descripcion = models.CharField(max_length=200, null=False)
    imagen = models.ImageField(upload_to='photos', default="", null=True)
    producto = models.ManyToManyField(Producto, blank=True,through='MenuProducto')

    def __str__(self):
        return f"{self.nombre_menu}: {self.precio_variable}"

class MenuProducto(models.Model):
    menu = models.ForeignKey(Menu,on_delete=models.CASCADE,null=True, blank=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True, blank=True)

class Restaurante(models.Model):
    nombre = models.CharField(max_length=30)
    telefono = models.PositiveIntegerField()
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu,on_delete=models.CASCADE)

class Sede(models.Model):
    direccion_sede = models.CharField(max_length=30)
    restaurante = models.ForeignKey(Restaurante,on_delete=models.CASCADE)