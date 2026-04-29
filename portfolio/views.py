from django.shortcuts import render
from .models import Licenciatura, UnidadeCurricular, Tecnologia, Projeto, TFC, Competencia, Docente, Formacao, MakingOf

def licenciatura_view(request):

    licenciatura = Licenciatura.objects.select_related('docentes').all()

    return render(request, 'portfolio/licenciatura.html',{'licenciatura':licenciatura})

def unidadeCurricular_view(request):

    unidadeCurricular = UnidadeCurricular.objects.select_related('docentes').prefetch_related('licenciatura').all()

    return render(request, 'portfolio/unidadeCurricular.html',{'unidadeCurricular':unidadeCurricular})

def tecnologia_view(request):

    tecnologia = Tecnologia.objects.select_related('unidades_curriculares').all()

    return render(request, 'portfolio/tecnologia.html',{'tecnologia':tecnologia})

def competencia_view(request):

    competencia = Competencia.objects.all()

    return render(request, 'portfolio/competencia.html',{'competencia':competencia})

def projeto_view(request):

    projeto = Projeto.objects.select_related('tecnologias').select_related('competencias').prefetch_related('unidade_curricular').all()

    return render(request, 'portfolio/projeto.html',{'projeto':projeto})

def tfc_view(request):

    tfc = TFC.objects.select_related('tecnologias').all()

    return render(request, 'portfolio/tfc.html',{'tfc':tfc})

def formacao_view(request):

    formacao = Formacao.objects.select_related('tecnologias').all()

    return render(request,'portfolio/formacao.html',{'formacao':formacao})

def makingof_view(request):

    makingof = MakingOf.objects.all()

    return render(request,'portfolio/makingof.html',{'makingof':makingof})