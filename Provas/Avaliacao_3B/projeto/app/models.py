from django.db import models

# Create your models here.
class Autor(models.Model):
    nome = models.CharField(max_length=200, null=False)
    biografia = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.nome

class Livro(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200, unique=True, null=False)
    ano_publicacao = models.IntegerField(null=False)
    arquivo_pdf = models.CharField(max_length=300 ,blank=True, null=True)
    descricao = models.TextField(max_length=300, null=False)
    
    def __str__(self):
        return self.titulo
    
class LivroTag(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name='tags') # Chave estrangeira de Livro
    tag = models.CharField(max_length=100, null=False)