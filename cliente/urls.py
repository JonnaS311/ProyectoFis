from django.contrib import admin
from django.urls import path
from .views import login, rotonda, menu_adder

urlpatterns = [
    path('', login),
    path('rotonda/', rotonda),
    path('menuadder/', menu_adder),
]
