from .models import Menu

def aniadir_menu(query):
    menu = Menu(nombre_menu = query.get("nombre"), precio_variable = int(query.get("precio")),
                descripcion = query.get("descripcion"), imagen = query.get("imagen"))
    menu.save()