from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    data_nascimento = models.DateTimeField("date published")
# Create your models here.

class Professor(models.Model):
    none = models.CharField(max_length=200)
    
class Curso(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    # Chave estrangeira para Curso
    curso=models.ForeignKey(Curso, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, null=True)
    nome=models.CharField(max_length=200)
    codigo=models.CharField(max_length=6, null=True)
    
    # Definindo uma relação muitos para muitos
    alunos = models.ManyToManyField(Aluno)
    
class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    periodo = models.IntegerField(null=True)
