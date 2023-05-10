from django import forms
from .models import Producto

class Crear_Menu(forms.Form):
    nombre = forms.CharField(max_length=50)
    imagen = forms.ImageField()
    descripcion = forms.CharField(max_length=200)
    precio = forms.IntegerField()
    productos = forms.ModelMultipleChoiceField(queryset=Producto.objects.all())
