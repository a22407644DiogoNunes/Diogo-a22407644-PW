from django import forms
from .models import Projeto, Tecnologia, Competencia, Formacao

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = [
            'nome',
            'descricao',
            'imagem',
            'video',
            'link_github',
            'unidade_curricular',
            'tecnologias',
            'competencias'
        ]

        widgets = {
            'tecnologias': forms.CheckboxSelectMultiple(),
            'competencias': forms.CheckboxSelectMultiple(),
        }

class TecnologiaForm(forms.ModelForm):
    class Meta:
        model=Tecnologia

        fields = [
            'nome',
            'descricao',
            'interesse_pessoal',
            'link_site',
            'imagem'
        ] 

        widgets = {
            'unidades_curriculares': forms.CheckboxSelectMultiple(),
        }

class CompetenciaForm(forms.ModelForm):
    class Meta:
        model=Competencia

        fields = [
            'nome',
            'descricao'
        ]

class Formacao(forms.ModelForm):
    class Meta:
        model=Formacao

        fields = [
            'nome',
            'instituicao',
            'descricao'
        ]

        widgets = {
            'tecnologias': forms.CheckboxSelectMultiple(),
        }