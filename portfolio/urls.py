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
    path('sobre_esta_aplicacao/',views.sobre_esta_aplicacao_view ,name = "sobre_esta_aplicacao"),

    path('projeto/novo', views.novo_projeto_view, name="novo_projeto"),
    path('tecnologia/novo', views.novo_tecnologia_view, name="novo_tecnologia"),
    path('competencia/novo', views.novo_competencia_view, name="novo_competencia"),
    path('formacao/novo', views.novo_formacao_view, name="novo_formacao"),

    path('projeto/<int:projeto_id>/edita', views.edita_projeto_view,name="edita_projeto"),
    path('tecnologia/<int:tecnologia_id>/edita', views.edita_tecnologia_view,name="edita_tecnologia"),
    path('competencia/<int:competencia_id>/edita', views.edita_competencia_view,name="edita_competencia"),
    path('formacao/<int:formacao_id>/edita', views.edita_formacao_view,name="edita_formacao"),

    path('projeto/<int:projeto_id>/apaga', views.apaga_projeto_view, name = "apaga_projeto"),
    path('tecnologia/<int:tecnologia_id>/apaga', views.apaga_tecnologia_view, name = "apaga_tecnologia"),
    path('competencia/<int:competencia_id>/apaga', views.apaga_competencia_view, name = "apaga_competencia"),
    path('formacao/<int:formacao_id>/apaga', views.apaga_formacao_view, name = "apaga_formacao")
]