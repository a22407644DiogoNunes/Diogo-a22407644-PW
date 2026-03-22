from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Escola (models.Model):
    nome = models.CharField(max_length = 50)
    localizacao = models.CharField(max_length = 100)

    def __str__(self):
        return f'{self.nome} - {self.localizacao}'

class Turma (models.Model):
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE)
    ano = models.IntegerField()
    turma = models.CharField(max_length = 1)

    def __str__(self):
        return f'{self.escola} - {self.ano}º{self.turma}'
    
class Professor (models.Model):
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    cadeira = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.turma} - {self.nome} - {self.cadeira}'
    
class Aluno (models.Model):
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    numero = models.CharField(max_length=8, unique=True)

    def __str__(self):
        return f'{self.turma} - {self.nome} - {self.numero}'