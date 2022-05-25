from sre_constants import SUCCESS
from urllib import request
import django
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Serie
from .forms import FormSerie
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, UpdateView


def buscarSerie(request):
    return render(request, "paginas/buscarSerie.html")



def buscarS(request):
    #respuesta = f"Estoy buscando la serie {request.GET['nombre']}"
    if request.GET.get("nombre"):                                           #Si el nombre existe entonces
        nombre = request.GET.get("nombre")                                  #almaceno ese nombre
        #series = Serie.objects.filter(nombre__icontains=nombre)            #filtro o busco por las letras que contiene el nombre en la DB
        series = Serie.objects.filter(nombre__iexact=nombre)                #filtro o busco por el nombre exacto en la DB
        return render(request, "paginas/busquedaS.html", {"serie": series}) 

    return render(request, "paginas/buscarSerie.html")


def serie(request):
    tvserie = Serie.objects.all()
    return render(request, "paginas/series.html", {"serie": tvserie})

def login(request):
    tvserie = Serie.objects.all()
    return render(request, "paginas/login.html", {"serie": tvserie})



def ver_serie(request, codserie, ):
    tvserie  = Serie.objects.get(codserie=codserie)
    return render(request, "paginas/ver_serie.html", {"serie": tvserie})


def nueva_serie(request):
    if request.method == "POST":
        mi_form = FormSerie(request.POST)
        if mi_form.is_valid():
            info = mi_form.cleaned_data
            tvserie = Serie(
                codserie=info["codserie"],
                nombre=info["nombre"],
                tipo=info["tipo"],
                plataforma=info["plataforma"],
                fecha=info["fecha"],
                episodio=info["episodio"],
                temporada=info["temporada"],
                terminada=info["terminada"],
                sinopsis=info["sinopsis"],    
            )
            tvserie.save()
            return redirect("SerieList")

    mi_form = FormSerie()

    return render(request, "paginas/serie_form.html", {"form": mi_form})


#Se agregan Vistas basadas en clases

class SerieList(ListView):
    model = Serie
    template_name = "/paginas/series.html"

class SerieDelete(DeleteView):
    model = Serie
    success_url = "/paginas/series"

class SerieUpdate(UpdateView):
    model = Serie
    success_url = "/paginas/series"
    fields = ['codserie','nombre','tipo','plataforma','fecha','episodio','temporada','terminada','sinopsis']