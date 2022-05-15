from django.db import models

class Serie(models.Model):
    nombre = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    plataforma = models.CharField(max_length=255)
    fecha = models.DateField(default=2000)
    episodio = models.IntegerField()
    temporada = models.IntegerField()
    terminada = models.BooleanField()
    sinopsis = models.TextField()
    codserie = models.CharField(max_length=25, null=True, blank=True, default=None)
 
    def __str__(self):
        return f"{self.nombre} {self.codserie}"

