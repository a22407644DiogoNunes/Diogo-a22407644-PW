from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import Artigo, Comentario
from .forms import ArtigoForm, ComentarioForm


def artigos_view(request):
    artigos = Artigo.objects.select_related('autor').prefetch_related('comentarios').all().order_by('-data_criacao')
    return render(request, 'artigos/artigos.html', {'artigos': artigos})


def artigo_detalhe_view(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    comentarios = artigo.comentarios.select_related('autor').all()
    form = ComentarioForm()
    return render(request, 'artigos/artigo_detalhe.html', {
        'artigo': artigo,
        'comentarios': comentarios,
        'form': form,
    })


def is_autor(user):
    return user.groups.filter(name='autores').exists()


@login_required
def novo_artigo_view(request):
    if not is_autor(request.user):
        raise PermissionDenied

    form = ArtigoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        artigo = form.save(commit=False)
        artigo.autor = request.user
        artigo.save()
        return redirect('artigos')

    return render(request, 'artigos/novo_artigo.html', {'form': form})


@login_required
def edita_artigo_view(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)

    if not is_autor(request.user) or artigo.autor != request.user:
        raise PermissionDenied

    form = ArtigoForm(request.POST or None, request.FILES or None, instance=artigo)
    if form.is_valid():
        form.save()
        return redirect('artigos')

    return render(request, 'artigos/edita_artigo.html', {'form': form, 'artigo': artigo})


@login_required
def apaga_artigo_view(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)

    if not is_autor(request.user) or artigo.autor != request.user:
        raise PermissionDenied

    artigo.delete()
    return redirect('artigos')


@login_required
def like_artigo_view(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)

    if request.user in artigo.likes.all():
        artigo.likes.remove(request.user)
    else:
        artigo.likes.add(request.user)

    return redirect('artigo_detalhe', artigo_id=artigo_id)


@login_required
def novo_comentario_view(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.artigo = artigo
            comentario.autor = request.user
            comentario.save()

    return redirect('artigo_detalhe', artigo_id=artigo_id)