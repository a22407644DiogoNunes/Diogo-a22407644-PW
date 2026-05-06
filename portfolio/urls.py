from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio_home, name="portfolio_home"),
    path('licenciaturas/', views.licenciatura_view, name="licenciatura"),
    path('unidades-curriculares/', views.unidadeCurricular_view, name="unidadeCurricular"),
    path('docentes/', views.docente_view, name="docente"),
    path('tecnologias/', views.tecnologia_view, name="tecnologia"),
    path('projetos/', views.projeto_view, name="projeto"),
    path('tfc/', views.tfc_view, name="tfc"),
    path('formacoes/', views.formacao_view, name="formacao"),
    path('competencias/', views.competencia_view, name="competencia"),
    path('makingof/', views.makingof_view, name="makingOf"),
    path('projeto/novo', views.novo_projeto_view, name="novo_projeto"),
    path('tecnologia/novo', views.novo_tecnologia_view, name="novo_tecnologia"),
    path('competencia/novo', views.novo_competencia_view, name="novo_competencia"),
    path('formacao/novo', views.novo_formacao_view, name="novo_formacao"),
]