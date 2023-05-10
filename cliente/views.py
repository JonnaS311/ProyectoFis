from django.http import HttpResponse
from django.shortcuts import render
from .form import aniadir_menu
from .models import Producto
def login(request):
    #https://www.flaticon.es/packs/food-and-restaurant-9
    return render(request, template_name='login.html')

def rotonda(request):
    return render(request, template_name='rotonda.html')

def menu_adder(request):
    List = list(Producto.objects.all())
    print(List)
    if request.method == "POST":
        aniadir_menu(request.POST)
    return render(request,template_name='menu_add.html',context={'productos':List})