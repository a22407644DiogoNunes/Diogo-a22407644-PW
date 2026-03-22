from django.db import models

# Create your models here.
class Utilizador(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=12)

    def __str__(self):
        return f'{self.nome} - {self.email}'

class Ingrediente(models.Model):
    nomeIngrediente = models.CharField(max_length=50)
    quantidade = models.IntegerField()

    def __str__(self):
        return f'{self.nomeIngrediente} - {self.quantidade}'

class Receita (models.Model):
    nome = models.CharField(max_length=25)
    ingredientes = models.ManyToManyField(Ingrediente, related_name='ingrediente')
    utilizadores = models.ManyToManyField(Utilizador, related_name='utilizador')

    def __str__(self):
        return f'{self.nome}'