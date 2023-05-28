from django.contrib import admin
from .models import Cliente
from django.contrib.auth.models import Group, Permission

# Register your models here.

admin.site.register(Cliente)

# Crea un grupo para los restaurantes
#restaurante_group, created = Group.objects.get_or_create(name='Restaurante')

# Asigna los permisos correspondientes al grupo
#restaurante_group.permissions.add(
#    Permission.objects.get(codename='is_restaurant'),
#)