from django.contrib import admin
from .models import Licenciatura,Docente
# Register your models here.

class DocenteAdmin(admin.ModelAdmin):
    list_display = ("nome", "email",)
    ordering = ("nome",)
    search_fields = ("nome", "email",)

admin.site.register(Docente, DocenteAdmin)

class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ("nome", "grau", "duracao",)
    ordering = ("nome",)
    search_fields = ("nome",)
admin.site.register(Licenciatura, LicenciaturaAdmin)