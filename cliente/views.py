from django.http import HttpResponse
from django.shortcuts import render
from .logic import aniadir_menu, aniadir_producto
from .models import Menu
from .forms import Crear_Menu, Crear_Producto, Crear_Cliente


def login(request):
    #https://www.flaticon.es/packs/food-and-restaurant-9
    return render(request, template_name='login.html')

def register(request):
    #https://www.flaticon.es/packs/food-and-restaurant-9
    if request.method == "POST":

        formulario = Crear_Cliente(request.POST,request.FILES)
        if formulario.is_valid():
            infForm = formulario.cleaned_data
            ##aniadir_menu(infForm)
    else:
        formulario = Crear_Cliente()
    return render(request, template_name='register.html', context={'form':formulario})

def rotonda(request):
    return render(request, template_name='rotonda.html',context={'menus':Menu.objects.all()})

def menu_adder(request):

    if request.method == "POST":

        formulario = Crear_Menu(request.POST,request.FILES)
        if formulario.is_valid():
            infForm = formulario.cleaned_data
            aniadir_menu(infForm)
    else:
        formulario = Crear_Menu()
    return render(request,"menu_add.html", context={'form':formulario})

def producto_adder(request):

    if request.method == "POST":

        formulario = Crear_Producto(request.POST,request.FILES)
        if formulario.is_valid():
            print("es valido")
            infForm = formulario.cleaned_data
            aniadir_producto(infForm)
    else:
        formulario = Crear_Producto()
    return render(request,"producto_add.html", context={'form':formulario})