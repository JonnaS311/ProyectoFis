import datetime

from django.contrib.auth.hashers import make_password

from .models import Menu, MenuProducto, Producto, Restaurante


def agregar_menu(query, restaurante):
    menu = Menu(nombre_menu = query.get("nombre"), precio_variable = int( query.get("precio")),
                descripcion = query.get("descripcion"), imagen = query.get("imagen"),
                restaurante = Restaurante.objects.get(id=restaurante))
    # Sumatoria del precio
    rel_menu_producto = list()
    precio = query.get("precio")
    menor_disponibilidad = list()
    for i in query.get("productos"):
        precio += int(i.precio_fijo)
        menor_disponibilidad.append(i.disponibilidad)
        rel_menu_producto.append(MenuProducto(menu=menu,producto=i))
    menu.precio_variable = precio
    menu.disponibilidad = min(menor_disponibilidad)
    menu.save()
    MenuProducto.objects.bulk_create(rel_menu_producto)


def agregar_producto(query, restaurante):
    producto = Producto(nombre_producto = query.get("nombre"), precio_fijo = int(query.get("precio")),
                        imagen = query.get("imagen"),restaurante = Restaurante.objects.get(id=restaurante),
                        disponibilidad = query.get("cantidad"))
    print(producto)
    producto.save()


def editar_menu(query):
    menu = query.get("menu")

    if query.get("nombre") != '':
        menu.nombre_menu = query.get('nombre')
    if query.get("imagen") is not None:
        menu.imagen = query.get('imagen')
    if query.get("descripcion") != '':
        menu.descripcion = query.get('descripcion')
    if query.get("precio") is not None:
        menu.precio_variable += query.get("precio")
    if query.get("productos").exists():
        precio = menu.precio_variable
        MenuProducto.objects.filter(menu_id=menu.pk).delete()
        rel_menu_producto = list()
        for i in query.get("productos"):
            precio += int(i.precio_fijo)
            rel_menu_producto.append(MenuProducto(menu=menu, producto=i))
        MenuProducto.objects.bulk_create(rel_menu_producto)
        menu.precio_variable = precio
        menu.disponibilidad = menor_cantidad(menu)
    menu.save()

def editar_producto(query):
    producto = query.get("producto")
    if query.get("nombre") != '':
        producto.nombre_producto = query.get('nombre')
        print(producto.nombre_producto)
    if query.get("imagen") is not None:
        producto.imagen = query.get("imagen")
    if query.get("precio") is not None:
        menus = MenuProducto.objects.filter(producto_id=producto.pk)
        lista_menus = set()
        for i in menus:
            menu = Menu.objects.get(id=i.menu_id)
            if not (menu in lista_menus):
                menu.precio_variable = menu.precio_variable - producto.precio_fijo + query.get('precio')
                lista_menus.add(menu)
        producto.precio_fijo = query.get('precio')
        Menu.objects.bulk_update(lista_menus,['precio_variable'])
    if query.get("cantidad") is not None:
        producto.disponibilidad = query.get("cantidad")
        producto.save()
        lista_menus = set()
        menus = MenuProducto.objects.filter(producto_id=producto.pk)
        for i in menus:
            menu = Menu.objects.get(id=i.menu_id)
            menu.disponibilidad = menor_cantidad(menu)
            lista_menus.add(menu)
        Menu.objects.bulk_update(lista_menus, ['disponibilidad'])
    producto.save()
def crear_restaurante(info):
    # Hash de la contraseña
    password_hash = make_password(info['password'])

    # Crear instancia del cliente
    restaurante = Restaurante(nombre=info['nombre'], password=password_hash, telefono=info['telefono'],
                      especialidad=info['especialidad'])
    restaurante.save()

def menor_cantidad(menu):
    lista_productos = list()
    for i in MenuProducto.objects.filter(menu_id=menu.pk):
        lista_productos.append( Producto.objects.get(id=i.producto_id).disponibilidad)
    print(lista_productos)
    return min(lista_productos)