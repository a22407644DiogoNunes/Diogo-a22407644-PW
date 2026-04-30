from django.shortcuts import render
from .models import Licenciatura, UnidadeCurricular, Tecnologia, Projeto, TFC, Competencia, Docente, Formacao, MakingOf

def portfolio_home(request):
    return render(request, 'portfolio/home.html')

def licenciatura_view(request):

    licenciatura = Licenciatura.objects.prefetch_related('docentes').all()

    return render(request, 'portfolio/licenciatura.html',{'licenciatura':licenciatura})

def docente_view(request):

    docente = Docente.objects.all()

    return render(request, 'portfolio/docente.html',{'docente':docente})

def unidadeCurricular_view(request):

    unidadeCurricular = UnidadeCurricular.objects.select_related('licenciatura').prefetch_related('docentes').all()

    return render(request, 'portfolio/unidadeCurricular.html',{'unidadeCurricular':unidadeCurricular})

def tecnologia_view(request):

    tecnologia = Tecnologia.objects.prefetch_related('unidades_curriculares').all()

    return render(request, 'portfolio/tecnologia.html',{'tecnologia':tecnologia})

def competencia_view(request):

    competencia = Competencia.objects.all()

    return render(request, 'portfolio/competencia.html',{'competencia':competencia})

def projeto_view(request):

    projeto = Projeto.objects.select_related('unidade_curricular').prefetch_related('tecnologias', 'competencias').all()

    return render(request, 'portfolio/projeto.html',{'projeto':projeto})

def tfc_view(request):

    tfc = TFC.objects.prefetch_related('tecnologias').all()

    return render(request, 'portfolio/tfc.html',{'tfc':tfc})

def formacao_view(request):

    formacao = Formacao.objects.prefetch_related('tecnologias').all()

    return render(request,'portfolio/formacao.html',{'formacao':formacao})

def makingof_view(request):

    makingof = MakingOf.objects.all()

    return render(request,'portfolio/makingof.html',{'makingof':makingof})