from django.contrib import admin

from .models import Producto, MenuProducto, Menu

# Register your models here.
admin.site.register(Producto)
admin.site.register(MenuProducto)
admin.site.register(Menu)