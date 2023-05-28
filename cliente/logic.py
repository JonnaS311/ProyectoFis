from restaurante.models import Menu

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