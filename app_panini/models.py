from django.db import models

# Create your models here.

class Seleccion(models.Model):
    nombre = models.CharField(max_length=100)
    grupo = models.CharField(max_length=1)
    escudo = models.ImageField(upload_to='escudos/')
    bandera = models.ImageField(upload_to='banderas/')

    def __str__(self):
        return self.nombre

class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    posicion = models.CharField(max_length=50)
    numero = models.IntegerField()
    alias = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='jugadores/')
    seleccion = models.ForeignKey(Seleccion, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre