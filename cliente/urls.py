from django.contrib import admin
from django.urls import path
from .views import login, rotonda, register

urlpatterns = [
    path('', login),
    path('register/', register),
    path('rotonda/', rotonda),
]
