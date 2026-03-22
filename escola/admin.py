from django.contrib import admin
from .models import Escola,Turma,Professor,Aluno

# Register your models here.
class EscolaAdmin(admin.ModelAdmin):
    list_display = ("nome","localizacao",)
    ordering = ("nome",)
    search_fields = ("nome",)

admin.site.register(Escola,EscolaAdmin)

class TurmaAdmin(admin.ModelAdmin):
    list_display = ("escola__nome","ano","turma",)
    ordering = ("ano",)

admin.site.register(Turma,TurmaAdmin)

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ("nome","cadeira","turma__ano","turma__turma")
    ordering = ("nome",)

admin.site.register(Professor,ProfessorAdmin)

class AlunoAdmin(admin.ModelAdmin):
    list_display = ("nome","numero","turma__ano","turma__turma")
    ordering = ("nome",)

admin.site.register(Aluno,AlunoAdmin)