from django.shortcuts import render
from .models import anime_favorito

def inicio(request):
    return render(request, 'Home.html')

def brayan(request):
    cajaAnime = anime_favorito.objects.all()
    return render(request, 'Brayan.html', {'animes': cajaAnime})
    