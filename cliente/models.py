from django.db import models


class Pedido(models.Model):
    fecha = models.DateField()
    estado = models.CharField(max_length=30)
    #sede = models.ForeignKey(Sede, on_delete=models.CASCADE)

class Client(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=30,default="", null=False)
    telefono = models.PositiveIntegerField()
    direccion_cliente = models.CharField(max_length=30)
    pedido = models.ForeignKey(Pedido,on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"nombre: {self.name}, telefono: {self.telefono}, direccion: {self.direccion_cliente}"
