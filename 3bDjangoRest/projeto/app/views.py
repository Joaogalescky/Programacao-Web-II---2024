# Importações
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Usuario, Medicamento, Prescricao
from .serializers import UsuarioSerializer, MedicamentoSerializer, PrescricaoSerializer

# CRUD - Usuário
class UsuarioView(APIView):
    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request):
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class UsuarioReadUpdateDeleteView(APIView):
    def get(self, request, id):
        usuario = get_object_or_404(Usuario, pk=id)
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        usuario = get_object_or_404(Usuario, pk=id)
        serializer = UsuarioSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        usuario = get_object_or_404(Usuario, pk=id)
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# CRUD - Medicamento
class MedicamentoView(APIView):
    def post(self, request):
        serializer = MedicamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        medicamentos = Medicamento.objects.all()
        serializer = MedicamentoSerializer(medicamentos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class MedicamentoReadUpdateDeleteView(APIView):
    def get(self, request, id):
        medicamento = get_object_or_404(Medicamento, pk=id)
        serializer = MedicamentoSerializer(medicamento)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        medicamento = get_object_or_404(Medicamento, pk=id)
        serializer = MedicamentoSerializer(medicamento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        medicamento = get_object_or_404(Medicamento, pk=id)
        medicamento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# CRUD - Prescrição
class PrescricaoCreateWithMedicamentoView(APIView):
    def post(self, request):
        medicamento_data = request.data.pop('medicamento')
        medicamento_serializer = MedicamentoSerializer(data=medicamento_data)
    
        if medicamento_serializer.is_valid():
            medicamento = medicamento_serializer.save()
            
            # Vincular a prescrição ao medicamento
            prescricao_data = request.data
            prescricao_data['medicamento'] = medicamento.id # Associa o medicamento
            prescricao_serializer = PrescricaoSerializer(data=prescricao_data)
            
            if prescricao_serializer.is_valid():
                prescricao_serializer.save()
                return Response(prescricao_serializer.data, status=status.HTTP_201_CREATED)
            return Response(prescricao_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(medicamento_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        prescricoes = Prescricao.objects.all()
        serializer = PrescricaoSerializer(prescricoes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)