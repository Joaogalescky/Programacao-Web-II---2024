from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Autor, Livro, Tag
from .serializers import AutorSerializer, LivroSerializer, TagSerializer

# Create your views here.
# CRUD - Autor
class AutorView(APIView):
    # POST
    def post(self, request):
        serializer = AutorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
    # GET
    def get(self, request):
        autores = Autor.objects.all()
        serializer = AutorSerializer(autores, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class AutorReadUpdateDeleteView(APIView):
    # GET
    def get(self, request, id):
        autor = get_object_or_404(Autor, pk=id)
        serializer = AutorSerializer(autor)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # PUT
    def put(self, request, id):
        autor = get_object_or_404(Autor, pk=id)
        serializer = AutorSerializer(autor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # DELETE
    def delete(self, request, id):
        autor = get_object_or_404(Autor, pk=id)
        autor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# CRUD - Livro
class LivroView(APIView):
    # POST
    def post(self, request):
        serializer = LivroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # GET
    def get(self, request):
        livros = Livro.objects.all()
        serializer = LivroSerializer(livros, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class LivroReadUpdateDeleteView(APIView):
    # GET
    def get(self, request, id):
        livro = get_object_or_404(Livro, pk=id)
        serializer = LivroSerializer(livro)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # PUT
    def put(self, request, id):
        livro = get_object_or_404(Livro, pk=id)
        serializer = LivroSerializer(livro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # DELETE
    def delete(self, request, id):
        livro = get_object_or_404(Livro, pk=id)
        livro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LivroCreateWithAutorView(APIView):
    # POST
    def post(self, request):
        autor_data = request.data.pop('autor')
        livro_data = request.data
    
        # Serializar o autor (caso seja novo)
        autor_serializer = AutorSerializer(data=autor_data)
        if autor_serializer.is_valid():
            autor = autor_serializer.save()
            livro_data = request.data.copy()
            livro_data['autor'] = autor.id

            livro_serializer = LivroSerializer(data=livro_data)
            if livro_serializer.is_valid():
                livro_serializer.save()
                return Response(livro_serializer.data, status=status.HTTP_201_CREATED)

            return Response(livro_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(autor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# CRUD - Tag
class TagCreateWithLivroView(APIView):
    # POST
    def post(self, request):
        tags_data = request.data.pop('tags')
        livro_data = request.data
    
        livro_serializer = LivroSerializer(data=livro_data)
        if livro_serializer.is_valid():
            livro = livro_serializer.save()
            
            # Vincular a tag ao livro
            for tag_data in tags_data:
                tag, created = Tag.objects.get_or_create(nome=tag_data['nome'])
                livro.tags.add(tag)
            return Response(LivroSerializer(livro).data, status=status.HTTP_201_CREATED)
        return Response(livro_serializer.errors, status=status.HTTP_400_BAD_REQUEST)