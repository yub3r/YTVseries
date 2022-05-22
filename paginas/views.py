from urllib import request
import django
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Serie
from .forms import FormSerie



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
    # else:
    #     respuesta = "No enviaste datos"
    
    # return HttpResponse(respuesta)



def serie(request):
    tvserie = Serie.objects.all()
    return render(request, "paginas/series.html", {"serie": tvserie})


def ver_serie(request, nombre):
    tvserie  = Serie.objects.get(nombre=nombre)
    return render(request, "paginas/ver_serie.html", {"serie": tvserie})


def nueva_serie(request):
    if request.method == "POST":
        mi_form = FormSerie(request.POST)
        if mi_form.is_valid():
            info = mi_form.cleaned_data
            tvserie = Serie(
                nombre=info["nombre"],
                tipo=info["tipo"],
                plataforma=info["plataforma"],
                fecha=info["fecha"],
                episodio=info["episodio"],
                temporada=info["temporada"],
                terminada=info["terminada"],
                sinopsis=info["sinopsis"],
                codserie=info["codserie"],
            )
            tvserie.save()
            return redirect("ListaSeries")

    mi_form = FormSerie()

    return render(request, "paginas/formSerie.html", {"form": mi_form})

