from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    data_nascimento = models.DateTimeField("date published")
# Create your models here.
    
class Curso(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    curso=models.ForeignKey(Curso, on_delete=models.CASCADE)
    nome=models.CharField(max_length=200)
    codigo=models.CharField(max_length=6, null=True)
