from django.shortcuts import render
from .models import Seleccion

def inicio(request):
    return render(request, 'Home.html')

def selecciones(request):
    cajaSelecciones=Seleccion.objects.all()
    return render(request, 'selecciones.html', {'selecciones': cajaSelecciones})