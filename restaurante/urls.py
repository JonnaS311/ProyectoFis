from django.contrib import admin
from django.urls import path
from .views import menu_adder, producto_adder, inicio, menu_edit

urlpatterns = [
    path('menuadder/', menu_adder, name='menu_adder'),
    path('productoadder/', producto_adder, name='producto_adder'),
    path('menueditor/', menu_edit, name='menu_editor'),
    path('', inicio, name='inicio'),
]
