from django.contrib import admin
from .models import Licenciatura,Docente,UnidadeCurricular,Tecnologia,Competencia,Projeto,TFC,Formacao
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

class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    ordering = ("nome",)
    search_fields = ("nome",)
admin.site.register(Competencia, CompetenciaAdmin)

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ("nome", "unidade_curricular",)
    list_filter = ("unidade_curricular",)
    ordering = ("nome",)
    search_fields = ("nome", "descricao",)
admin.site.register(Projeto, ProjetoAdmin)

class TFCAdmin(admin.ModelAdmin):
    list_display = ("nome", "ano", "orientadores",)
    list_filter = ("ano",)
    ordering = ("-ano", "nome",)
    search_fields = ("nome", "orientadores",)
admin.site.register(TFC,TFCAdmin)

class FormacaoAdmin(admin.ModelAdmin):
    list_display = ("nome", "instituicao",)
    ordering = ("nome",)
    search_fields = ("nome", "instituicao",)
admin.site.register(Formacao,FormacaoAdmin)