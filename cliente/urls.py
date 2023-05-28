from django.contrib import admin
from django.urls import path
from .views import login_app, rotonda, register, exit, carrito

urlpatterns = [
    path('', login_app, name='login'),
    path('register/', register, name = 'register'),
    path('rotonda/', rotonda, name='rotonda'),
    path('carrito/', carrito, name='carrito'),
    path('logout/', exit, name='exit'),

]
