from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Treino, Exercicio
from .serializers import TreinoSerializer, ExercicioSerializer

# Exercicio Views
class ExercicioView(APIView):
    # POST - Criar exercício
    def post(self, request):
        serializer = ExercicioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # GET - Listar exercícios
    def get(self, request):
        exercicios = Exercicio.objects.all()
        serializer = ExercicioSerializer(exercicios, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ExercicioTreinoReadUpdateDelete(APIView):
    # GET - Detalhar exercício por ID
    def get(self, request, pk):
        exercicio = get_object_or_404(Exercicio, pk=pk)
        serializer = ExercicioSerializer(exercicio)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # PUT - Atualizar exercício
    def put(self, request, pk):
        exercicio = get_object_or_404(Exercicio, pk=pk)
        serializer = ExercicioSerializer(exercicio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE - Remover exercício
    def delete(self, request, pk):
        exercicio = get_object_or_404(Exercicio, pk=pk)
        exercicio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Treino Views
class TreinoExercicioView(APIView):
    # POST - Criar treino com múltiplos exercícios
    def post(self, request):
        serializer = TreinoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # GET - Listar todos os treinos
    def get(self, request):
        treinos = Treino.objects.all()
        serializer = TreinoSerializer(treinos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TreinoReadView(APIView):
    # GET - Detalhar treino por ID (inclui exercícios associados)
    def get(self, request, pk):
        treino = get_object_or_404(Treino, pk=pk)
        serializer = TreinoSerializer(treino)
        return Response(serializer.data, status=status.HTTP_200_OK)