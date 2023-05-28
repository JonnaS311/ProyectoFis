from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect

from .forms import Crear_Menu, Crear_Producto, Editar_Menu, Editar_Producto, Crear_Restaurante
from .logic import agregar_menu, agregar_producto, editar_menu, editar_producto, crear_restaurante


# Create your views here.
@login_required
#@permission_required('Restaurante.is_restaurant')
def menu_adder(request):

    if request.method == "POST":

        formulario = Crear_Menu(request.POST,request.FILES)
        if formulario.is_valid():
            infForm = formulario.cleaned_data
            agregar_menu(infForm,request.user.id)
    else:
        formulario = Crear_Menu()
    return render(request,"menu_add.html", context={'form':formulario})

@login_required
#@permission_required('Restaurante.is_restaurant')
def menu_edit(request):
    if request.method == "POST":
        formulario = Editar_Menu(request.POST,request.FILES)
        if formulario.is_valid():
            infForm = formulario.cleaned_data
            editar_menu(infForm)
    else:
        formulario = Editar_Menu()
    return render(request,"editor.html", context={'form':formulario,'text':"Personaliza tus menús a tu antojo"})

@login_required
#@permission_required('Restaurante.is_restaurant')
def producto_adder(request):
    if request.method == "POST":
        formulario = Crear_Producto(request.POST,request.FILES)
        if formulario.is_valid():
            infForm = formulario.cleaned_data
            agregar_producto(infForm,request.user.id)
    else:
        formulario = Crear_Producto()
    return render(request,"producto_add.html", context={'form':formulario})

@login_required
#@permission_required('Restaurante.is_restaurant')
def producto_edit(request):
    if request.method == "POST":

        formulario = Editar_Producto(request.POST,request.FILES)
        if formulario.is_valid():
            infForm = formulario.cleaned_data
            editar_producto(infForm)
    else:
        formulario = Editar_Producto()
    return render(request,"editor.html", context={'form':formulario,'text':"Personaliza tus productos a tu antojo"})

@login_required
#@permission_required('Restaurante.is_restaurant')
def inicio(request):
    return render(request,"inicio.html")

def login_rest(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Verificar las credenciales del usuario
        print(username," + ", password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            # Iniciar sesión
            login(request, user)
            return redirect('inicio')  # Cambia la URL por la deseada
        else:
            # Las credenciales son inválidas, mostrar un mensaje de error o redirigir a otra página
            return redirect('login_rest')
    return render(request,"./registration/login_restaurante.html")

def register(request):
    if request.method == "POST":
        formulario = Crear_Restaurante(request.POST,request.FILES)
        if formulario.is_valid():
            infForm = formulario.cleaned_data
            print(infForm)
            crear_restaurante(infForm)
    else:
        formulario = Crear_Restaurante()
    return render(request,"register_restaurante.html",context={'form':formulario})
def exit_rest(request):
    logout(request)
    return redirect('login_rest')