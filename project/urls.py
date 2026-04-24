## ficheiro projects/urls.py

from django.contrib import admin
from django.urls import path, include              #     <- adicionar include 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),    
    path("cursos/", include("cursos.urls")), 
    path("", include("cursos.urls")),
]

# Sere ficheiros media em DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)