from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Autor, Livro
from .serializers import AutorSerializer, LivroAutorSerializer


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
    def get(self, request, pk):
        autor = get_object_or_404(Autor, pk=pk)
        serializer = AutorSerializer(autor)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # PUT
    def put(self, request, pk):
        autor = get_object_or_404(Autor, pk=pk)
        serializer = AutorSerializer(autor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE
    def delete(self, request, pk):
        autor = get_object_or_404(Autor, pk=pk)
        autor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# CRUD - Livro com Autor e Tags aninhados
class LivroAutorView(APIView):
    # POST
    def post(self, request):
        serializer = LivroAutorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # GET
    def get(self, request):
        livros = Livro.objects.all()
        serializer = LivroAutorSerializer(livros, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class LivroAutorReadUpdateDelete(APIView):
    # GET
    def get(self, request, pk):
        livro = get_object_or_404(Livro, pk=pk)
        serializer = LivroAutorSerializer(livro)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # PUT
    def put(self, request, pk):
        livro = get_object_or_404(Livro, pk=pk)
        serializer = LivroAutorSerializer(livro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE
    def delete(self, request, pk):
        livro = get_object_or_404(Livro, pk=pk)
        livro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)