from django.contrib import admin
from django.urls import path, include
# 1. Importa los ajustes del proyecto y la función static
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), # Corregido de admin.site.admin a admin.site.urls
    path('', include('app_panini.urls')),
]

# 2. Conecta la ruta de medios si estás en modo desarrollo (DEBUG = True)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
