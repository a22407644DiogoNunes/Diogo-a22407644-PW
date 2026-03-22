from django.db import models

# Create your models here.
class Festival (models.Model):
    nome = models.CharField(max_length=25)
    data = models.DateField()
    localizacao = models.CharField(max_length=50)

    def __str__ (self):
        return f'{self.nome} no {self.localizacao} ás {self.data}'
    
class Genero (models.Model):
    tipo = models.CharField(15)

    def __str__ (self):
        return f'{self.tipo}'
    

    
class Banda (models.Model):
    nome = models.CharField(max_length=25)
    generoMusical = models.ForeignKey(Genero, on_delete=models.CASCADE)
    festivais = models.ManyToManyField(Festival, related_name='festival')
    
    def __str__ (self):
        return f'{self.nome} - {self.generoMusical}'
    
