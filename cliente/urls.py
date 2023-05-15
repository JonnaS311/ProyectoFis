from django.contrib import admin
from django.urls import path
from .views import login, rotonda, menu_adder, producto_adder, register

urlpatterns = [
    path('', login),
    path('register/', register),
    path('rotonda/', rotonda),
    path('menuadder/', menu_adder),
    path('productoadder/', producto_adder),
]
