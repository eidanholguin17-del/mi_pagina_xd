from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('Brayan/', views.brayan, name='brayan'),
    path('subir-anime/', views.subir_anime, name='subir_anime'),

]