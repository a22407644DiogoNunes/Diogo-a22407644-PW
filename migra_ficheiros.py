import os
from django.core.files import File
from django.conf import settings

MEDIA_ROOT = settings.MEDIA_ROOT

# Portfolio
from portfolio.models import Projeto, Tecnologia, UnidadeCurricular, MakingOf

for obj in Projeto.objects.all():
    if obj.imagem and obj.imagem.name:
        local_path = os.path.join(MEDIA_ROOT, obj.imagem.name)
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.imagem.save(os.path.basename(local_path), File(f), save=True)
            print(f"Migrado: {obj}")

for obj in Tecnologia.objects.all():
    if obj.imagem and obj.imagem.name:
        local_path = os.path.join(MEDIA_ROOT, obj.imagem.name)
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.imagem.save(os.path.basename(local_path), File(f), save=True)
            print(f"Migrado: {obj}")

for obj in UnidadeCurricular.objects.all():
    if obj.imagem and obj.imagem.name:
        local_path = os.path.join(MEDIA_ROOT, obj.imagem.name)
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.imagem.save(os.path.basename(local_path), File(f), save=True)
            print(f"Migrado: {obj}")

for obj in MakingOf.objects.all():
    if obj.foto_papel and obj.foto_papel.name:
        local_path = os.path.join(MEDIA_ROOT, obj.foto_papel.name)
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.foto_papel.save(os.path.basename(local_path), File(f), save=True)
            print(f"Migrado: {obj}")