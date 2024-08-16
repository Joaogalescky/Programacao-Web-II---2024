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