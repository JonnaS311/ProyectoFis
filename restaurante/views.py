from django.shortcuts import render

from .forms import Crear_Menu, Crear_Producto, Editar_Menu
from .logic import agregar_menu, agregar_producto, editar_menu


# Create your views here.
def menu_adder(request):

    if request.method == "POST":

        formulario = Crear_Menu(request.POST,request.FILES)
        if formulario.is_valid():
            infForm = formulario.cleaned_data
            agregar_menu(infForm)
    else:
        formulario = Crear_Menu()
    return render(request,"menu_add.html", context={'form':formulario})

def menu_edit(request):
    if request.method == "POST":

        formulario = Editar_Menu(request.POST,request.FILES)
        if formulario.is_valid():
            infForm = formulario.cleaned_data
            editar_menu(infForm)
    else:
        formulario = Editar_Menu()
    return render(request,"menu_editor.html", context={'form':formulario})

def producto_adder(request):

    if request.method == "POST":

        formulario = Crear_Producto(request.POST,request.FILES)
        if formulario.is_valid():
            print("es valido")
            infForm = formulario.cleaned_data
            agregar_producto(infForm)
    else:
        formulario = Crear_Producto()
    return render(request,"producto_add.html", context={'form':formulario})

def inicio(request):

    return render(request,"inicio.html")