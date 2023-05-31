from django import forms
from .models import Producto, Menu


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
    cantidad = forms.IntegerField()

class Editar_Menu(forms.Form):
    menu = forms.ModelChoiceField(queryset=Menu.objects.all())
    nombre = forms.CharField(max_length=50,required=False)
    imagen = forms.ImageField(required=False)
    descripcion = forms.CharField(max_length=200,required=False)
    precio = forms.IntegerField(required=False)
    productos = forms.ModelMultipleChoiceField(queryset=Producto.objects.all(),required=False)

    def __init__(self ,query=None,*args, **kwargs):
        super().__init__(*args, **kwargs)
        modificar = query
        campos = ('nombre','imagen','descripcion','precio','productos')
        if modificar is not None:
            for i in modificar:
                if i in campos:
                    self.fields[i].widget.attrs['disabled'] = 'disabled'

class Editar_Producto(forms.Form):
    producto = forms.ModelChoiceField(queryset=Producto.objects.all())
    nombre = forms.CharField(max_length=50,required=False)
    imagen = forms.ImageField(required=False)
    precio = forms.IntegerField(min_value=0,required=False)
    cantidad = forms.IntegerField(min_value=0,required=False)

    def __init__(self ,query=None,*args, **kwargs):
        super().__init__(*args, **kwargs)
        modificar = query
        campos = ('nombre', 'imagen', 'precio', 'cantidad')
        if modificar is not None:
            for i in modificar:
                if i in campos:
                    self.fields[i].widget.attrs['disabled'] = 'disabled'

class Crear_Restaurante(forms.Form):
    nombre = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    telefono = forms.IntegerField(max_value=9999999999, min_value=1000000000)
    especialidad = forms.CharField(max_length=50)