from rest_framework import serializers
from .models import Autor, Livro, Tag

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'
        
class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'
                
class TagSerializer(serializers.ModelSerializer):
    autor = serializers.PrimaryKeyRelatedField(queryset=Autor.objects.all())
    livro = serializers.PrimaryKeyRelatedField(queryset=Livro.objects.all())
    
    class Meta:
        model = Tag
        fields = '__all__'

# Objeto Aninhado - Autor e Livro
class AutorLivroCreateUpdateSerializer(serializers.ModelSerializer):
    livros = LivroSerializer(many=True,  required=False)
    class Meta:
        model = Autor
        fields = '__all__'
        read_only_fields = ['id']
        
    def create(self, validated_data):
        livros_data = validated_data.pop('livros', [])

        autor = Autor.objects.create(**validated_data)

        for livro_data in livros_data:

            Autor.objects.create(autor=autor, **livro_data)
        return autor

# Objeto Aninhado - Livro e Tag
class LivroTagCreateUpdateSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True,  required=False)
    class Meta:
        model = Livro
        fields = '__all__'
        read_only_fields = ['id']
        
    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])

        livro = Livro.objects.create(**validated_data)

        for tag_data in tags_data:

            Livro.objects.create(livro=livro, **tag_data)
        return livro