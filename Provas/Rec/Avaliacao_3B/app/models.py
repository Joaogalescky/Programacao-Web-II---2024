from django.db import models

# Create your models here.
class Exercicio(models.Model):
    nome = models.CharField(max_length=200, null=False)
    descricao_execucao = models.TextField(blank=False)

    def __str__(self):
        return self.nome

class Treino(models.Model):
    data_inicio = models.DateField()
    data_fim = models.DateField()
    objetivo = models.CharField(max_length=50, null=False)
    exercicios = models.ManyToManyField(Exercicio, related_name='treinos')
    
    def __str__(self):
        return self.objetivo
