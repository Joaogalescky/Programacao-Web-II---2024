from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

#importando modelos e serializers
from .models import Professor, Curso, Disciplina
from .serializers import ProfessorSerializer, CursoSerializer, DisciplinaSerializer, DisciplinaCreateUpdateSerializer

# Create your views here.
class ProfessorView(APIView):

    # Define as ações quando recebe um requisicao do tipo post
    
    # POST
    def post(self, request):

        # Instancia o serialize com os dados recebidos no 'request'
        serializer = ProfessorSerializer(data = request.data)
        if serializer.is_valid():

            # Se o formato recebido estiver correto, salva os dados no banco de dados
            serializer.save()

            # Retorna com o codigo 201 e os dados do serializer
            return Response(serializer.data, status = status.HTTP_201_CREATED)

        # Se o serializer não for valido, retorna erro 400
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    # GET
    def get(self, request):
        professors = Professor.objects.all()
        serializer = ProfessorSerializer(professors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ProfessorReadUpdateDeleteView(APIView):
# View para recuperar, atualizar ou deletar um professor específico.

    # GET
    def get(self, request, id):
        professor = get_object_or_404(Professor, pk=id)
        
        '''
            try:
                professor = Professor.objects.get(pk=pk)
            except Professor.DoesNotExist:
                return Response({'detail': 'Professor não encontrado.'}, status=status.HTTP_404_NOT_FOUND)
        '''
        
        serializer = ProfessorSerializer(professor)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # PUT
    def put(self, request, id):
        professor = get_object_or_404(Professor, pk=id)
        serializer = ProfessorSerializer(professor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # DELETE
    def delete(self, request, id):
        professor = get_object_or_404(Professor, pk=id)
        professor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CursoListCreateAPIView(APIView):
    
    # GET
    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # POST
    def post(self, request):
        serializer = CursoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DisciplinaRetrieveUpdateDestroyAPIView(APIView):
    
    # GET
    def get(self, request, id):
        try:
            disciplina = Disciplina.objects.get(pk=id)
        except Disciplina.DoesNotExist:
            return Response({'detail': 'Disciplina não encontrada.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = DisciplinaSerializer(disciplina)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # PUT
    def put(self, request, id):
        try:
            disciplina = Disciplina.objects.get(pk=id)
        except Disciplina.DoesNotExist:
            return Response({'detail': 'Disciplina não encontrada.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = DisciplinaCreateUpdateSerializer(disciplina, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE
    def delete(self, request, id):
        try:
            disciplina = Disciplina.objects.get(pk=id)
        except Disciplina.DoesNotExist:
            return Response({'detail': 'Disciplina não encontrada.'}, status=status.HTTP_404_NOT_FOUND)
        
        disciplina.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 