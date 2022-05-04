from urllib import request
import django
from django.shortcuts import render
from django.http import HttpResponse
from .models import Serie

def inicio(request):
    return HttpResponse("Hola mundo")

def buscar_serie(request):
    if request.GET.get("nombre"):
        nombre = request.GET.get("nombre")
        series = Serie.objects.filter(nombre__icontains=nombre)
        return render(request, "paginas/busqueda.html", {"serie": series})
    return render(request, "paginas/buscar.html")
