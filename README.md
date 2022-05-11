# YTVseries

Inicios de construcción de sitio web dedicado a Series de TV, donde críticos podran postear articulos sobre una serie y usarios podran hacer votaciones.

Incialmente se crean tres models o tablas:


# Usuario
nombre = models.CharField(max_length=255)
apellido = models.CharField(max_length=255)
email = models.EmailField()
alias = models.CharField(max_length=25)

# Critico
nombre = models.CharField(max_length=255)
apellido = models.CharField(max_length=255)
email = models.EmailField()
alias = models.CharField(max_length=25)
experiencia = models.TextField()

# Series 
nombre = models.CharField(max_length=255)
tipo = models.CharField(max_length=255)
plataforma = models.CharField(max_length=255)
fecha = models.DateField(default=2000)
episodio = models.IntegerField()
temporada = models.IntegerField()
terminada = models.BooleanField()
sinopsis = models.TextField()
codserie = models.CharField(max_length=25, default=None)


# Para la administracion:
http://127.0.0.1:8000/admin/

user: admin
pass: YTVS.123

