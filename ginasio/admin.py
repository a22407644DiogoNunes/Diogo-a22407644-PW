from django.contrib import admin
from .models import Ginasio,Pt,Membro,Agenda

# Register your models here.
class GinasioAdmin(admin.ModelAdmin):
    list_display = ("nome","localizacao",)
    ordering = ("nome",)
    search_fields = ("nome",)

admin.site.register(Ginasio,GinasioAdmin)

class PtAdmin(admin.ModelAdmin):
    list_display = ("nome","ptNumero",)
    ordering = ("ptNumero",)
    search_fields = ("nome",)

admin.site.register(Pt,PtAdmin)

class MenbroAdmin(admin.ModelAdmin):
    list_display = ("nome","nif",)
    ordering = ("nif",)
    search_fields = ("nome","nif",)

admin.site.register(Membro,MenbroAdmin)

class AgendaAdmin(admin.ModelAdmin):
    list_display = ("data", "hora",)
    ordering = ("data",)
    search_fields = ("data",)

admin.site.register(Agenda,AgendaAdmin)