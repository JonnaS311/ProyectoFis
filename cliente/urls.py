from django.contrib import admin
from django.urls import path
from .views import login_app, rotonda, register, exit

urlpatterns = [
    path('', login_app, name='login'),
    path('register/', register),
    path('rotonda/', rotonda, name='rotonda'),
    path('logout/', exit, name='exit'),
]
