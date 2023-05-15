from .models import Menu, MenuProducto, Producto

def aniadir_menu(query):
    menu = Menu(nombre_menu = query.get("nombre"), precio_variable = int(query.get("precio")),
                descripcion = query.get("descripcion"), imagen = query.get("imagen"))
    menu.save()
    for i in query.get("productos"):
        rel_menu_producto = MenuProducto(menu=menu,producto=i)
        rel_menu_producto.save()

def aniadir_producto(query):
    producto = Producto(nombre_producto = query.get("nombre"), precio_fijo = int(query.get("precio")),
                imagen = query.get("imagen"))
    producto.save()