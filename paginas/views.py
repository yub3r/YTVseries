from sre_constants import SUCCESS
from urllib import request
import django
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Serie
from .forms import FormSerie
from django.views.generic import ListView 
from django.views.generic.edit import DeleteView, UpdateView
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin #Necesario si es usa vistas basadas en clases
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login


def login_request(request):

    if request.method == 'POST': #al presionar el botón "Iniciar Sesión"
        loginform = AuthenticationForm(request, data = request.POST) #leer la data del formulario de inicio de sesión
        if loginform.is_valid():       
            usuario=loginform.cleaned_data.get('username')   #leer el usuario ingresado
            passw=loginform.cleaned_data.get('password')    #leer la contraseña ingresada

            user=authenticate(username=usuario, password=passw)    #buscar al usuario con los datos ingresados

            if user:    #si ha encontrado un usuario con eso datos
                login(request, user)   
                return render(request, "paginas/inicio.html", {'mensaje':f"Bienvenido {user}"}) 

        else:   
            return render(request, "paginas/inicio.html", {'mensaje':"Error. Datos incorrectos"})

    else:
        loginform = AuthenticationForm() #mostrar el formulario

    return render(request, "paginas/login.html", {'form':loginform})




def inicio(request):
    return render(request, "paginas/inicio.html")

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

# def login(request):
#     tvserie = Serie.objects.all()
#     return render(request, "paginas/login.html", {"serie": tvserie})

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