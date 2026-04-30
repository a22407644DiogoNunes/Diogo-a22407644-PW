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
]