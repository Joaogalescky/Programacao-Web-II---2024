from rest_framework import serializers
from .models import Professor, Curso, Disciplina, ConteudoProgramatico

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

class ConteudoProgramaticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConteudoProgramatico
        fields = ['descricao']

# Objeto Aninhado
class DisciplinaConteudoCreateUpdateSerializer(serializers.ModelSerializer):
    conteudos_programaticos = ConteudoProgramaticoSerializer(many=True,  required=False)
    '''
    Objetivo deste código é permitir que, ao criar uma disciplina, também consiga adicionar, 
    de maneira organizada, múltiplos conteúdos programáticos associados a ela. 
    Elimina a necessidade de fazer chamadas separadas para criar os conteúdos programáticos,
    tornando a criação mais eficiente e simplificada.
    '''
    class Meta:
        model = Disciplina
        fields = ['id','curso', 'professor', 'nome', 'codigo', 'conteudos_programaticos']
        read_only_fields = ['id']
        
    # É sobrescrito para personalizar o processo de criação do objeto Disciplina
    def create(self, validated_data):
        conteudos_data = validated_data.pop('conteudos_programaticos', []) # conteudos_programaticos - fazendo isso, não é necessário utilizar o _set para buscar a classe filho/filha
        '''
        pop - remove o campo do dicionário de 'conteudos_programaticos',
        permitindo que os dados restantes sejam usados para criar a instância de Disciplina
        '''
        disciplina = Disciplina.objects.create(**validated_data)
        '''
        cria um novo objeto Disciplina usando os dados restantes
        '''
        for conteudo_data in conteudos_data:
            '''
            Um loop percorre os dados de conteúdos programáticos e cria cada instância de ConteudoProgramatico,
            associando-a à disciplina recém-criada.
            '''
            ConteudoProgramatico.objects.create(disciplina=disciplina, **conteudo_data)
        return disciplina