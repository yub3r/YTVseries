from urllib import request
import django
from django.shortcuts import render
from django.http import HttpResponse
from .models import Serie

def inicio(request):
    return HttpResponse("Hola mundo")

def buscar_serie(request, codserie):
        if request.GET.get("nombre"):
            nombre = request.GET.get("nombre")
            series = Serie.objects.filter(nombre__icontains=nombre, codserie=codserie)
            return render(request, "paginas/busqueda.html", {"series": series})
     
     
     
        return render(request, "paginas/buscar.html")
