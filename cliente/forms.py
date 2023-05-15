from django import forms

from .models import Producto

class Crear_Menu(forms.Form):
    nombre = forms.CharField(max_length=50)
    imagen = forms.ImageField()
    descripcion = forms.CharField(max_length=200)
    precio = forms.IntegerField()
    productos = forms.ModelMultipleChoiceField(queryset=Producto.objects.all())

class Crear_Producto(forms.Form):
    nombre = forms.CharField(max_length=50)
    imagen = forms.ImageField()
    precio = forms.IntegerField()

class Crear_Cliente(forms.Form):
    nombre = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    telefono = forms.IntegerField(max_value=9999999999, min_value=1000000000)
    direccion = forms.CharField(max_length=50)