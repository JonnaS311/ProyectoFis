from django import forms

class Crear_Cliente(forms.Form):
    nombre = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    telefono = forms.IntegerField(max_value=9999999999, min_value=1000000000)
    direccion = forms.CharField(max_length=50)