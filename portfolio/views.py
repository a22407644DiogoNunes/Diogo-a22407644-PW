from django.shortcuts import redirect, render
from .models import Licenciatura, UnidadeCurricular, Tecnologia, Projeto, TFC, Competencia, Docente, Formacao, MakingOf
from .forms import ProjetoForm, TecnologiaForm, CompetenciaForm, FormacaoForm

#-------------------------------------------------------------------------------------#

def portfolio_home(request):
    return render(request, 'portfolio/home.html')

#-------------------------------------------------------------------------------------#

def licenciatura_view(request):

    licenciatura = Licenciatura.objects.prefetch_related('docentes').all()

    return render(request, 'portfolio/licenciatura.html',{'licenciatura':licenciatura})

#-------------------------------------------------------------------------------------#

def docente_view(request):

    docente = Docente.objects.all()

    return render(request, 'portfolio/docente.html',{'docente':docente})

#-------------------------------------------------------------------------------------#

def unidadeCurricular_view(request):

    unidadeCurricular = UnidadeCurricular.objects.select_related('licenciatura').prefetch_related('docentes').all()

    return render(request, 'portfolio/unidadeCurricular.html',{'unidadeCurricular':unidadeCurricular})

#-------------------------------------------------------------------------------------#

def tecnologia_view(request):

    tecnologia = Tecnologia.objects.prefetch_related('unidades_curriculares').all()

    return render(request, 'portfolio/tecnologia.html',{'tecnologia':tecnologia})

def novo_tecnologia_view(request):
    form = TecnologiaForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('tecnologia')
    
    context = {'form': form}
    return render(request, 'portfolio/novo_tecnologia.html', context)

def edita_tecnologia_view(request, tecnologia_id):
    tecnologia = Tecnologia.objects.get(id=tecnologia_id)
    
    if request.POST:
        form = TecnologiaForm(request.POST or None, request.FILES, instance=tecnologia)
        if form.is_valid():
            form.save()
            return redirect('tecnologia')
    else:
        form = TecnologiaForm(instance=tecnologia)  # cria formulário com dados da instância autor
        
    context = {'form': form, 'tecnologia':tecnologia}
    return render(request, 'portfolio/edita_tecnologia.html', context)

def apaga_tecnologia_view(request, tecnologia_id):
    tecnologia = Tecnologia.objects.get(id = tecnologia_id)
    tecnologia.delete()
    return redirect('tecnologia')

#-------------------------------------------------------------------------------------#

def competencia_view(request):

    competencia = Competencia.objects.all()

    return render(request, 'portfolio/competencia.html',{'competencia':competencia})

def novo_competencia_view(request):
    form = CompetenciaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('competencia')
    
    context = {'form': form}
    return render(request, 'portfolio/novo_competencia.html', context)

def edita_competencia_view(request, competencia_id):
    competencia = Competencia.objects.get(id=competencia_id)

    if request.POST:
        form = CompetenciaForm(request.POST or None, request.FILES, instance=competencia)
        if form.is_valid():
            form.save()
            return redirect('competencia')
        else:
            form = CompetenciaForm(instance=competencia)

        context = {'form': form, 'competencia':competencia}
        return render(request, 'portfolio/edita_competencia.html', context)

def apaga_competencia_view(request, competencia_id):
    competencia = Competencia.objects.get(id = competencia_id)
    competencia.delete()
    return redirect('competencia')

#-------------------------------------------------------------------------------------#

def projeto_view(request):

    projeto = Projeto.objects.select_related('unidade_curricular').prefetch_related('tecnologias', 'competencias').all()

    return render(request, 'portfolio/projeto.html',{'projeto':projeto})

def novo_projeto_view(request):
    form = ProjetoForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('projeto')
    
    context = {'form': form}
    return render(request, 'portfolio/novo_projeto.html', context)

def edita_projeto_view(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)

    if request.POST:
        form = ProjetoForm(request.POST or None, request.FILES, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('projeto')
        else:
            form = ProjetoForm(instance=projeto)

        context = {'form': form, 'projeto':projeto}
        return render(request, 'portfolio/edita_projeto.html', context)

def apaga_projeto_view(request, projeto_id):
    projeto = Projeto.objects.get(id = projeto_id)
    projeto.delete()
    return redirect('projeto')

#-------------------------------------------------------------------------------------#

def tfc_view(request):

    tfc = TFC.objects.prefetch_related('tecnologias').all()

    return render(request, 'portfolio/tfc.html',{'tfc':tfc})

#-------------------------------------------------------------------------------------#

def formacao_view(request):

    formacao = Formacao.objects.prefetch_related('tecnologias').all()

    return render(request,'portfolio/formacao.html',{'formacao':formacao})

def novo_formacao_view(request):
    form = FormacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('formacao')
    
    context = {'form': form}
    return render(request, 'portfolio/novo_formacao.html', context)

def edita_formacao_view(request, formacao_id):
    formacao = Formacao.objects.get(id=formacao_id)

    if request.POST:
        form = FormacaoForm(request.POST or None, request.FILES, instance=formacao)
        if form.is_valid():
            form.save()
            return redirect('formacao')
        else:
            form = FormacaoForm(instance=formacao)

        context = {'form': form, 'formacao':formacao}
        return render(request, 'portfolio/edita_formacao.html', context)

def apaga_formacao_view(request, formacao_id):
    formacao = Formacao.objects.get(id = formacao_id)
    formacao.delete()
    return redirect('formacao')

#-------------------------------------------------------------------------------------#

def makingof_view(request):

    makingof = MakingOf.objects.all()

    return render(request,'portfolio/makingof.html',{'makingof':makingof})