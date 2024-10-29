from rest_framework import serializers
from .models import Autor, Livro, LivroTag


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'


class LivroTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = LivroTag
        fields = ['tag']

class LivroAutorSerializer(serializers.ModelSerializer):
    autor = AutorSerializer()
    tags = LivroTagSerializer(many=True, write_only=True)  # Referência ao campo correto

    class Meta:
        model = Livro
        fields = ['id', 'titulo', 'ano_publicacao', 'descricao', 'autor', 'tags']

    def create(self, validated_data):
        autor_data = validated_data.pop('autor')
        autor, created = Autor.objects.get_or_create(**autor_data)
        tags_data = validated_data.pop('tags', [])
        
        # Criar o livro associado ao autor
        livro = Livro.objects.create(autor=autor, **validated_data)

        # Adicionar tags ao livro criado, utilizando o campo 'tag'
        for tag_data in tags_data:
            LivroTag.objects.create(livro=livro, tag=tag_data['tag'])  # Usando 'tag' corretamente
        return livro

    def update(self, instance, validated_data):
        # Atualização do autor
        autor_data = validated_data.pop('autor')
        autor, created = Autor.objects.get_or_create(**autor_data)
        instance.autor = autor

        # Atualização dos campos do livro
        instance.titulo = validated_data.get('titulo', instance.titulo)
        instance.ano_publicacao = validated_data.get('ano_publicacao', instance.ano_publicacao)
        instance.descricao = validated_data.get('descricao', instance.descricao)
        instance.save()

        # Atualização das tags
        tags_data = validated_data.pop('tags', [])
        instance.tags.all().delete()  # Remover as tags existentes

        for tag_data in tags_data:
            LivroTag.objects.create(livro=instance, tag=tag_data['tag'])
        return instance