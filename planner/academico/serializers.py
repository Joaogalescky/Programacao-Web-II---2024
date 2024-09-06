from rest_framework import serializers
from .models import Professor, Curso, Disciplina

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'
        
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['id', 'nome']
        
class DisciplinaSerializer(serializers.ModelSerializer):
    curso = CursoSerializer(read_only=True)
    professor = ProfessorSerializer(read_only=True)

    class Meta:
        model = Disciplina
        fields = ['id', 'nome', 'codigo', 'curso', 'professor']

class DisciplinaCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = ['id', 'nome', 'codigo', 'curso', 'professor']