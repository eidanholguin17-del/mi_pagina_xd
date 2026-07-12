from django.contrib import admin

# Register your models here.

from .models import Seleccion, Jugador

admin.site.register(Seleccion)
admin.site.register(Jugador)




