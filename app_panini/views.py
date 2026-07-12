from django.shortcuts import render, redirect # Añadimos redirect
from .models import anime_favorito

def inicio(request):
    return render(request, 'Home.html')

def brayan(request):
    cajaAnime = anime_favorito.objects.all()
    return render(request, 'Brayan.html', {'animes': cajaAnime})

# --- NUEVA VISTA PARA SUBIR LAS IMÁGENES ---
def subir_anime(request):
    if request.method == 'POST':
        # Capturamos los textos del formulario HTML
        anime_name = request.POST.get('anime')
        personaje_name = request.POST.get('personaje')
        
        # Capturamos los archivos de imagen
        portada = request.FILES.get('portada')
        logo = request.FILES.get('logo')
        
        # Guardamos en la base de datos usando tu modelo anime_favorito
        nuevo_anime = anime_favorito(
            anime=anime_name,
            personaje=personaje_name,
            Portada_Anime=portada,
            Logo_anime=logo
        )
        nuevo_anime.save()
        
        # Redirige a tu vista 'brayan' para ver la lista actualizada
        return redirect('brayan') 
        
    return render(request, 'subir_anime.html')
