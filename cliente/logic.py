from datetime import date
from restaurante.models import Menu
from django.contrib.auth.hashers import make_password
from .models import Cliente, Pedido

def crear_cliente(info):

    # Hash de la contraseña
    password_hash = make_password(info['password'])

    # Crear instancia del cliente
    cliente = Cliente(nombre=info['nombre'], password=password_hash, telefono=info['telefono'],
                      direccion=info['direccion'])
    cliente.save()



lista_carrito = set()
def cargar_carrito(id):
    lista_carrito.add(id)
    print(lista_carrito)

def get_carrito_compra():
    return Menu.objects.filter(id__in=lista_carrito)

def delete_carrito(id):
    lista_carrito.discard(id)

def cargar_menus():
    menus = get_carrito_compra()
    precio = 0
    for menu in menus:
        precio += menu.precio_variable
    precio *= 1.19
    return menus, precio

def generar_pedido(valor,cliente,act):
    if Cliente.objects.get(id=cliente).es_pagable == 1:
        pedido = Pedido(fecha = date.today(),estado = 'pago', pago = valor, cliente_id=cliente)
        lista_menus = list()
        for i in lista_carrito:
            menu = Menu.objects.get(id=i)
            if menu.disponibilidad > 0:
                menu.disponibilidad -= 1
                print(menu.disponibilidad)
                lista_menus.append(menu)
        pedido.save()
        Menu.objects.bulk_update(lista_menus,['disponibilidad'])
        lista_carrito.clear()
        print("se realizo el pedido")