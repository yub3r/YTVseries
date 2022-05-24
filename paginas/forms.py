from tkinter import Widget
from django import forms


class FormSerie(forms.Form):
    codserie = forms.CharField(max_length=25)
    nombre = forms.CharField(max_length=255)
    tipo = forms.CharField(max_length=255)
    plataforma = forms.CharField(max_length=255)
    fecha = forms.DateField()
    episodio = forms.IntegerField()
    temporada = forms.IntegerField()
    terminada = forms.BooleanField(required=False)
    sinopsis = forms.CharField(widget=forms.Textarea)
    

