from django.contrib import admin
from django.urls import path
from .views import menu_adder, producto_adder, inicio, menu_edit, producto_edit, login_rest, exit_rest, register

urlpatterns = [
    path('menuadder/', menu_adder, name='menu_adder'),
    path('productoadder/', producto_adder, name='producto_adder'),
    path('menueditor/', menu_edit, name='menu_editor'),
    path('productoeditor/', producto_edit, name='producto_editor'),
    path('inicio/', inicio, name='inicio'),
    path('register/', register, name='register_rest'),
    path('', login_rest, name='login_rest'),
    path('logout/', exit_rest, name='exit_rest'),
]
