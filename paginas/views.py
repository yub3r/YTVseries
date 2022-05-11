from urllib import request
import django
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Serie



def buscar_serie(request, codserie):
        if request.GET.get("nombre"):
            nombre = request.GET.get("nombre")
            series = Serie.objects.filter(nombre__icontains=nombre, codserie=codserie)
            return render(request, "paginas/busqueda.html", {"series": series})
     
        return render(request, "paginas/buscar.html")



# def serie(request):
#     tvserie = Serie.objects.all()
#     return render(request, "paginas/series.html", {"series": tvserie})


# def ver_serie(request, nombre):
#     tvserie  = Serie.objects.get(nombre=nombre)
#     return render(request, "paginas/ver_serie.html", {"series": tvserie})


# def nueva_serie(request):
#     if request.method == "POST":
#         mi_form = FormSerie(request.POST)
#         if mi_form.is_valid():
#             info = mi_form.cleaned_data
#             tvserie = Serie(
#                 nombre=info["nombre"],
#                 tipo=info["tipo"],
#                 plataforma=info["[plataforma]"],
#                 fecha=info["fecha"],
#                 episodio=info["episodio"],
#                 temporada=info["temporada"],
#                 terminada=info["terminada"],
#                 sinopsis=info["sinopsis"],
#                 codserie=info["codserie"],
#             )
#             tvserie.save()
#             return redirect("ListaSerie")

#     mi_form = FormSerie()

#     return render(request, "paginas/formSerie.html", {"form": mi_form})

