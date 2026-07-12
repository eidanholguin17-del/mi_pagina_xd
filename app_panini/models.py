from django.db import models

# Create your models here.

class anime_favorito(models.Model):
    anime = models.CharField(max_length=100)
    personaje = models.CharField(max_length=100)
    Portada_Anime = models.ImageField(upload_to='Portadas/')
    Logo_anime = models.ImageField(upload_to='animes_L/')

    def __str__(self):
        return self.anime

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    lvl_power = models.CharField(max_length=999)
    tier = models.IntegerField()
    apodo = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='jugadores/')
    seleccion = models.ForeignKey(anime_favorito, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre