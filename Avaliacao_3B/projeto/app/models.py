from django.db import models

# Create your models here.
class Autor(models.Model):
    nome = models.CharField(max_length=100, null=False)
    biografia = models.TextField(max_length=250, null=True)
    
    def __str__(self):
        return self.nome

class Livro(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE) # Chave estrangeira de Autor
    titulo = models.CharField(max_length=200, null=False)
    ano_publicacao = models.IntegerField(null=False)
    arquivo_pdf = models.CharField(max_length=100, null=False)
    descricao = models.TextField(max_length=300, null=False)
    
    def __str__(self):
        return self.nome
    
class Tag(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name='tags') # Chave estrangeira de Livro
    nome = models.CharField(max_length=50, null=False)