from django.shortcuts import render
from .forms import Crear_Cliente
from restaurante.models import Menu


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

