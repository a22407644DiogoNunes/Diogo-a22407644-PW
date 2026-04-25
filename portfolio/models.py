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
    duracao = models.CharField(max_length=50) # ex: "3 anos" ou "6 semestres"
    url_site = models.URLField()
    docentes = models.ManyToManyField(Docente, related_name="licenciaturas", null=True, blank=True)

    def __str__(self):
        return self.nome