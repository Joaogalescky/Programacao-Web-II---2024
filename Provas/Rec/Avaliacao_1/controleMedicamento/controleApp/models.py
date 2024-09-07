from django.db import models

# Create your models here.
class Paciente(models.Model):
    nome = models.CharField(max_length = 200, null=False)
    email = models.EmailField(max_length = 100, null=False, unique=True)
    telefone = models.CharField(max_length = 15, null=False)
    senha = models.CharField(max_length = 25, null=False)

    def __str__(self):
        return self.nome

class Medicamento(models.Model):
    nome = models.CharField(max_length = 200, null=False, unique=True)
    dosagem = models.CharField(max_length = 50, null=False)
    forma = models.CharField(max_length = 150, null=False) # Comprimido, Líquido, Injeção

    def __str__(self):
        return self.nome

class Prescricao(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    dataInicio = models.DateTimeField("Data de inicío", null=False)
    dataFim = models.DateTimeField("Data de término", null=False)
    frequenciaUso = models.CharField(max_length = 200, null=False)

    def __str__(self):
        return f"{self.paciente.nome} - {self.medicamento.nome}"

class Registro(models.Model):
    prescricao = models.ForeignKey(Prescricao, on_delete=models.CASCADE)
    horarioPrescrito = models.DateTimeField("Horário prescrito", null=False)
    horarioIngerido = models.DateTimeField("horário ingerido", null=True, blank=True)
    observacao = models.CharField(max_length = 200, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.prescricao.nome} - {self.horarioPrescrito.strftime('%Y-%m-%d %H:%M')}"
