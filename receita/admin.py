from django.contrib import admin
from .models import Receita,Utilizador,Ingrediente

# Register your models here.
class UtilizadorAdmin(admin.ModelAdmin):
    list_display = ("nome", "email")
    search_fields = ("nome", "email")
    ordering = ("nome",)

admin.site.register(Utilizador,UtilizadorAdmin)

class IngredienteAdmin(admin.ModelAdmin):
    list_display = ("nomeIngrediente", "quantidade")
    search_fields = ("nomeIngrediente",)
    ordering = ("nomeIngrediente",)

admin.site.register(Ingrediente,IngredienteAdmin)

class ReceitaAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)
    filter_horizontal = ("ingredientes", "utilizadores")

admin.site.register(Receita,ReceitaAdmin)