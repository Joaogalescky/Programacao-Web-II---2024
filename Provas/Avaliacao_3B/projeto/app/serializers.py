from rest_framework import serializers
from .models import Autor, Livro, Tag

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'
      
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
  
class LivroSerializer(serializers.ModelSerializer):
    autor = serializers.PrimaryKeyRelatedField(queryset=Autor.objects.all())  
    tags = TagSerializer(many=True, required=False)
    
    class Meta:
        model = Livro
        fields = '__all__'

    def create(self, validated_data):
        # Separar autor e tags dos dados validados
        autor = validated_data.pop('autor')
        tags_data = validated_data.pop('tags', [])
        
        # Criar o livro
        livro = Livro.objects.create(autor=autor, **validated_data)

        # Criar e associar as tags
        for tag_data in tags_data:
            tag, _ = Tag.objects.get_or_create(**tag_data)
            livro.tags.add(tag)

        return livro
    
    def update(self, instance, validated_data):
        # Atualizar os campos do livro (autor, título, ano_publicacao, etc.)
        instance.titulo = validated_data.get('titulo', instance.titulo)
        instance.ano_publicacao = validated_data.get('ano_publicacao', instance.ano_publicacao)
        instance.arquivo_pdf = validated_data.get('arquivo_pdf', instance.arquivo_pdf)
        instance.descricao = validated_data.get('descricao', instance.descricao)
        instance.autor = validated_data.get('autor', instance.autor)
        instance.save()

        # Atualizar as tags associadas
        tags_data = validated_data.get('tags', None)
        if tags_data:
            # Limpar as tags atuais
            instance.tags.clear()
            # Criar/associar novas tags
            for tag_data in tags_data:
                tag, _ = Tag.objects.get_or_create(**tag_data)
                instance.tags.add(tag)

        return instance