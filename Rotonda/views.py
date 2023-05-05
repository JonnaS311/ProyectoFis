from django.http import HttpResponse
from django.shortcuts import render

def login(request):
    #https://www.flaticon.es/packs/food-and-restaurant-9
    return render(request, template_name='login.html')

def rotonda(request):
    return render(request, template_name='rotonda.html')