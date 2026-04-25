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
    docentes = models.ManyToManyField(Docente, related_name="licenciaturas", null=True, blank=True)

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
    docentes = models.ManyToManyField(Docente, related_name="unidades_curriculares", null=True, blank=True)

    def __str__(self):
        return self.nome

class Tecnologia(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    interesse_pessoal = models.BooleanField(default=False)
    link_site = models.URLField(null=True, blank=True)
    imagem = models.ImageField(upload_to='tecnologias/', null=True, blank=True)
    unidades_curriculares = models.ManyToManyField(UnidadeCurricular, related_name="tecnologias", null=True, blank=True)

    def __str__(self):
        return self.nome