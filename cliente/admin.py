from django.contrib import admin
from .models import Menu, Client,Producto,MenuProducto

# Register your models here.

admin.site.register(Menu)
admin.site.register(Client)
admin.site.register(Producto)
admin.site.register(MenuProducto)