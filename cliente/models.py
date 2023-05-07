from django.db import models


class Ingrediente(models.Model):
    precio_fijo = models.IntegerField()

class Producto(models.Model):
    precio_fijo = models.IntegerField()
    #imagen = models.ImageField(upload_to='post/%Y/%m/%d')

class Menu(models.Model):
    precio_variable = models.IntegerField(null=False)
    nombre_menu = models.CharField(max_length=50, null=False, default="")
    descripcion = models.CharField(max_length=200, null=False, default="")
    imagen = models.ImageField(upload_to='photos', default="", null=True)
    #producto = models.ForeignKey(Producto,on_delete=models.CASCADE, null=True, default=None)
    #ingrediente = models.ForeignKey(Ingrediente,on_delete=models.CASCADE, null=True, default=None)

class Restaurante(models.Model):
    nombre = models.CharField(max_length=30)
    telefono = models.PositiveIntegerField()
    ingrediente = models.ForeignKey(Ingrediente,on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu,on_delete=models.CASCADE)

class Sede(models.Model):
    direccion_sede = models.CharField(max_length=30)
    restaurante = models.ForeignKey(Restaurante,on_delete=models.CASCADE)

class Pedido(models.Model):
    fecha = models.DateField()
    estado = models.CharField(max_length=30)
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE)

class Client(models.Model):
    name = models.CharField(max_length=30)
    telefono = models.PositiveIntegerField()
    direccion_cliente = models.CharField(max_length=30)
    pedido = models.ForeignKey(Pedido,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"nombre: {self.name}, telefono: {self.telefono}, direccion: {self.direccion_cliente}"
