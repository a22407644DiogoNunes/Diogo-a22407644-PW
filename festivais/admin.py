from django.contrib import admin
from .models import Festival,Banda,Genero

# Register your models here.
class FestivalAdmin (admin.ModelAdmin):
    list_display = ("nome","data","localizacao",)
    ordering = ("nome",)
    search_fields = ("nome",)

admin.site.register(Festival,FestivalAdmin)

class BandaAdmin (admin.ModelAdmin):
    list_display = ("nome","generoMusical",)
    ordering = ("nome",)
    search_fields = ("nome","generoMusical",)

admin.site.register(Banda,BandaAdmin)

class GeneroAdmin (admin.ModelAdmin):
    list_display = ("tipo",)
    ordering = ("tipo",)
    search_fields = ("tipo",)

admin.site.register(Genero,GeneroAdmin)