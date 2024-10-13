from django.db import models

# Create your models here.
class Autor(models.Model):
    nome = models.CharField(max_length=100, null=False)
    biografia = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.nome

class Tag(models.Model):
    nome = models.CharField(max_length=100, null=False)
    
    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=200, null=False)
    ano_publicacao = models.IntegerField(null=False)
    arquivo_pdf = models.CharField(max_length=50, null=False) #FileField - upload_to='livros/'
    descricao = models.TextField(null=False)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='livros')
    tags = models.ManyToManyField(Tag, blank=True, related_name='livros')
    
    def __str__(self):
        return self.titulo