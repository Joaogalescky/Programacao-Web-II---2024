from django.db import models

# Create your models here.

class Professor(models.Model):
    nome = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length = 200)
    sigla = models.CharField(max_length = 12)

    def __str__(self):
        return self.nome
    
class Disciplina(models.Model):
    #chave estrangeira para Curso.
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, null=True)
    nome = models.CharField(max_length=200)
    codigo = models.CharField(max_length=6, null=True)
    
class ConteudoProgramatico(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='conteudos_programaticos')
    descricao = models.TextField(null=True)