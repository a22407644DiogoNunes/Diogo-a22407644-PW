from django.contrib import admin
from .models import Licenciatura,Docente,UnidadeCurricular,Tecnologia
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

class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ("nome", "licenciatura", "ano", "semestre", "ects",)
    list_filter = ("licenciatura", "ano", "semestre",)
    ordering = ("ano", "semestre", "nome",)
    search_fields = ("nome",)
admin.site.register(UnidadeCurricular, UnidadeCurricularAdmin)

class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ("nome", "interesse_pessoal",)
    list_filter = ("interesse_pessoal",)
    ordering = ("nome",)
    search_fields = ("nome",)
admin.site.register(Tecnologia, TecnologiaAdmin)