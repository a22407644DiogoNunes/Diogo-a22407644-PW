from django.db import models

# Create your models here.
class Docente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.nome

class Licenciatura(models.Model):
    nome = models.CharField(max_length=100)
    grau = models.CharField(max_length=50)
    ects_totais = models.IntegerField()
    duracao = models.CharField(max_length=50)
    url_site = models.URLField()
    docentes = models.ManyToManyField(Docente, related_name="licenciaturas", blank=True)

    def __str__(self):
        return self.nome
    
class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=255)
    ects = models.IntegerField()
    descricao = models.TextField()
    ano = models.IntegerField()
    semestre = models.IntegerField()
    imagem = models.ImageField(upload_to='ucs/', null=True, blank=True)
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE, related_name="unidades_curriculares")
    docentes = models.ManyToManyField(Docente, related_name="unidades_curriculares", blank=True)

    def __str__(self):
        return self.nome

class Tecnologia(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    interesse_pessoal = models.BooleanField(default=False)
    link_site = models.URLField(null=True, blank=True)
    imagem = models.ImageField(upload_to='tecnologias/', null=True, blank=True)
    unidades_curriculares = models.ManyToManyField(UnidadeCurricular, related_name="tecnologias", blank=True)

    def __str__(self):
        return self.nome

class Competencia(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='projetos/', null=True, blank=True)
    video = models.URLField(null=True, blank=True)
    link_github = models.URLField()
    unidade_curricular = models.ForeignKey(UnidadeCurricular, on_delete=models.CASCADE, related_name="projetos")
    tecnologias = models.ManyToManyField(Tecnologia, related_name="projetos")
    competencias = models.ManyToManyField(Competencia, related_name="projetos")

    def __str__(self):
        return self.nome
    
class TFC(models.Model): # Trabalho de Fim de Curso
    nome = models.CharField(max_length=255)
    orientadores = models.TextField()
    ano = models.IntegerField()
    descricao = models.TextField()
    link_doc = models.URLField()
    tecnologias = models.ManyToManyField(Tecnologia, related_name="tfcs", blank=True)

    def __str__(self):
        return self.nome

class Formacao(models.Model):
    nome = models.CharField(max_length=255)
    instituicao = models.CharField(max_length=255)
    descricao = models.TextField()
    tecnologias = models.ManyToManyField(Tecnologia, related_name="formacoes", blank=True)

    def __str__(self):
        return self.nome