from django.db import models

# Create your models here.
class Paciente(models.Model):
    nome = models.CharField(max_length = 200, null=False)
    email = models.CharField(max_length = 100, null=False)
    telefone = models.CharField(max_length = 11, null=False)
    senha = models.CharField(max_length = 25, null=False)

class Medicamento(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=True)
    nome = models.CharField(max_length = 200, null=False)
    dosagem = models.CharField(max_length = 50, null=False)
    forma = models.CharField(max_length = 150, null=False)

class Prescricao(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    dataInicio = models.DateTimeField("data inicío publicada!", null=True)
    dataFim = models.DateTimeField("data fim publicada!", null=True)
    frequenciaUso = models.CharField(max_length = 200, null=False)

class Registro(models.Model):
    prescricao = models.ForeignKey(Prescricao, on_delete=models.CASCADE, null=True)
    horarioPrescrito = models.DateTimeField("horário prescrito publicado!", null=True)
    horarioIngerido = models.DateTimeField("horário ingerido publicado!", null=True)
    observacao = models.CharField(max_length = 200, null=True)
