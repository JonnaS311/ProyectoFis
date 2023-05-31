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
    formulario = Editar_Menu()
    if request.method == "POST":
        formulario = Editar_Menu(None, request.POST,request.FILES)
        print(formulario.is_valid())
        if formulario.is_valid():
            infForm = formulario.cleaned_data
            editar_menu(infForm)
            return redirect("menu_editor")
    elif request.method == "GET":
        formulario = Editar_Menu(query = request.GET)
    return render(request,"editor.html", context={'form':formulario,'text':"Personaliza tus menús a tu antojo",
                                                  'type':1})

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
    formulario = Editar_Producto()
    if request.method == "POST":
        formulario = Editar_Producto(None,request.POST,request.FILES)
        if formulario.is_valid():
            infForm = formulario.cleaned_data
            print(infForm)
            editar_producto(infForm)
            return redirect("producto_editor")
    elif request.method == "GET":
        formulario = Editar_Producto(query=request.GET)
    return render(request,"editor.html", context={'form':formulario,'text':"Personaliza tus productos a tu antojo",
                                                  'type':0})

@login_required
#@permission_required('Restaurante.is_restaurant')
def inicio(request):
    return render(request,"inicio.html")

def login_rest(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Verificar las credenciales del usuario
        user = authenticate(request, username=username, password=password)
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
            crear_restaurante(infForm)
    else:
        formulario = Crear_Restaurante()
    return render(request,"register_restaurante.html",context={'form':formulario})
def exit_rest(request):
    logout(request)
    return redirect('login_rest')