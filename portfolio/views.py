from django.shortcuts import redirect, render
from .models import Licenciatura, UnidadeCurricular, Tecnologia, Projeto, TFC, Competencia, Docente, Formacao, MakingOf
from .forms import ProjetoForm, TecnologiaForm, CompetenciaForm, FormacaoForm
from django.contrib.auth.decorators import login_required

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

    is_gestor = False

    if request.user.is_authenticated:
        is_gestor = request.user.groups.filter(
            name='gestor-portfolio'
        ).exists()

    context = {
        'tecnologia': tecnologia,
        'is_gestor': is_gestor,
    }

    return render(request, 'portfolio/tecnologia.html',context)

@login_required
def novo_tecnologia_view(request):
    form = TecnologiaForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('tecnologia')
    
    context = {'form': form}
    return render(request, 'portfolio/novo_tecnologia.html', context)

@login_required
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

@login_required
def apaga_tecnologia_view(request, tecnologia_id):
    tecnologia = Tecnologia.objects.get(id = tecnologia_id)
    tecnologia.delete()
    return redirect('tecnologia')

#-------------------------------------------------------------------------------------#

def competencia_view(request):

    competencia = Competencia.objects.all()

    is_gestor = False

    if request.user.is_authenticated:
        is_gestor = request.user.groups.filter(
            name='gestor-portfolio'
        ).exists()

    context = {
        'competencia': competencia,
        'is_gestor': is_gestor,
    }

    return render(request, 'portfolio/competencia.html',context)

@login_required
def novo_competencia_view(request):
    form = CompetenciaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('competencia')
    
    context = {'form': form}
    return render(request, 'portfolio/novo_competencia.html', context)

@login_required
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

@login_required
def apaga_competencia_view(request, competencia_id):
    competencia = Competencia.objects.get(id = competencia_id)
    competencia.delete()
    return redirect('competencia')

#-------------------------------------------------------------------------------------#

def projeto_view(request):

    projeto = Projeto.objects.select_related('unidade_curricular').prefetch_related('tecnologias', 'competencias').all()

    is_gestor = False

    if request.user.is_authenticated:
        is_gestor = request.user.groups.filter(
            name='gestor-portfolio'
        ).exists()

    context = {
        'projeto': projeto,
        'is_gestor': is_gestor,
    }

    return render(request, 'portfolio/projeto.html',context)

@login_required
def novo_projeto_view(request):
    form = ProjetoForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('projeto')
    
    context = {'form': form}
    return render(request, 'portfolio/novo_projeto.html', context)

@login_required
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

@login_required
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

    is_gestor = False

    if request.user.is_authenticated:
        is_gestor = request.user.groups.filter(
            name='gestor-portfolio'
        ).exists()

    context = {
        'formacao': formacao,
        'is_gestor': is_gestor,
    }

    return render(request,'portfolio/formacao.html',context)

@login_required
def novo_formacao_view(request):
    form = FormacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('formacao')
    
    context = {'form': form}
    return render(request, 'portfolio/novo_formacao.html', context)

@login_required
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

@login_required
def apaga_formacao_view(request, formacao_id):
    formacao = Formacao.objects.get(id = formacao_id)
    formacao.delete()
    return redirect('formacao')

#-------------------------------------------------------------------------------------#

def makingof_view(request):

    makingof = MakingOf.objects.all()

    return render(request,'portfolio/makingof.html',{'makingof':makingof})

#-------------------------------------------------------------------------------------#

def sobre_esta_aplicacao_view(request):
    from itertools import groupby
    from collections import defaultdict
 
    # Tecnologias agrupadas por tipo
    tecnologias = Tecnologia.objects.select_related('tipo').all().order_by('tipo__nome')
    tecnologias_por_tipo = defaultdict(list)
    for t in tecnologias:
        chave = t.tipo.get_nome_display() if t.tipo else 'Outros'
        tecnologias_por_tipo[chave].append(t)
 
    # Making Of
    makingof = MakingOf.objects.all().order_by('data_relatorio')
 
    context = {
        'tecnologias_por_tipo': dict(tecnologias_por_tipo),
        'makingof': makingof,
        # Preenche estes dois quando tiveres o URL da fotografia e do vídeo:
        # 'video_tutorial_url': 'https://www.youtube.com/embed/SEU_VIDEO_ID',
        'github_url': 'https://github.com/a22407644DiogoNunes/Diogo-a22407644-PW.git',
    }
    return render(request, 'portfolio/sobre_esta_aplicacao.html', context)
