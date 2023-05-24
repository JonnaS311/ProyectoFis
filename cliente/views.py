from django.shortcuts import render, redirect
from .forms import Crear_Cliente
from restaurante.models import Menu
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login


def login_app(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Verificar las credenciales del usuario
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Iniciar sesión
            login(request, user)
            return redirect('rotonda')  # Cambia la URL por la deseada
        else:
            # Las credenciales son inválidas, mostrar un mensaje de error o redirigir a otra página
            return redirect('login')
    return render(request, template_name='./registration/login.html')

def register(request):
    if request.method == "POST":
        formulario = Crear_Cliente(request.POST,request.FILES)
        if formulario.is_valid():
            infForm = formulario.cleaned_data
    else:
        formulario = Crear_Cliente()
    return render(request, template_name='register.html', context={'form':formulario})

@login_required
def rotonda(request):
    return render(request, template_name='rotonda.html',context={'menus':Menu.objects.all()})

@login_required
def carrito(request):
    menus = Menu.objects.all()
    precio = 0
    for menu in menus:
        precio += menu.precio_variable
    precio *= 1.19
    return render(request, template_name='carrito.html',context={'menus':menus,'precio_final':int(precio)})

def exit(request):
    logout(request)
    return redirect('login')