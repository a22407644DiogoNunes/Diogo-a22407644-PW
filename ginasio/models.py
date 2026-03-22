from django.db import models

# Create your models here.

class Ginasio(models.Model):
    nome = models.CharField(max_length=25)
    localizacao = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nome} - {self.localizacao}'

class Membro(models.Model):
    nome = models.CharField(max_length=50)
    nif = models.IntegerField()
    ginasio = models.ForeignKey(Ginasio, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} - {self.nif}'

class Pt(models.Model):
    nome = models.CharField(max_length=50)
    ptNumero = models.IntegerField()
    ginasio = models.ForeignKey(Ginasio, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} - {self.ptNumero}'
    
class Agenda(models.Model):
    data = models.DateField()
    hora = models.TimeField()
    pt = models.ForeignKey(Pt, on_delete=models.CASCADE)
    membro = models.ForeignKey(Membro, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.data} - {self.hora}'