from django.contrib import admin

from .models import Aluno,Curso, Disciplina
admin.site.register(Aluno)
admin.site.register(Curso)
admin.site.register(Disciplina)

# Register your models here.
