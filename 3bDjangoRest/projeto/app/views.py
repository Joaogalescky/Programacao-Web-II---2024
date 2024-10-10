from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Registro, Usuario, Medicamento, Prescricao
from .serializers import RegistroSerializer, UsuarioSerializer, MedicamentoSerializer, PrescricaoSerializer
from django.shortcuts import get_object_or_404

# CRUD Usuário
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
# CRUD Medicamento
class MedicamentoViewSet(viewsets.ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer

# Viewset Prescrições
class PrescricaoViewSet(viewsets.ModelViewSet):
    queryset = Prescricao.objects.all()
    serializer_class = PrescricaoSerializer

    @action(detail=False, methods=['post'])
    def cadastrar_prescricao_com_medicamento(self, request):
        """
        Este endpoint permite cadastrar uma prescrição e um medicamento ao mesmo tempo.
        """
        # Dados de paciente e medicamento
        paciente_id = request.data.get('paciente', {}).get('id')
        medicamento_data = request.data.get('medicamento')
        prescricao_data = request.data.copy()

        # Validação do paciente
        if not paciente_id:
            return Response({"error": "ID do paciente é obrigatório."}, status=status.HTTP_400_BAD_REQUEST)

        paciente = get_object_or_404(Usuario, id=paciente_id)
        
        # Verifica se o medicamento já existe, senão cria
        medicamento, created = Medicamento.objects.get_or_create(
            nome=medicamento_data['nome'],
            defaults={
                'dosagem': medicamento_data['dosagem'],
                'forma': medicamento_data['forma']
            }
        )

        # Adiciona IDs de paciente e medicamento aos dados da prescrição
        prescricao_data['paciente'] = paciente.id
        prescricao_data['medicamento'] = medicamento.id

        # Serializa e valida os dados da prescrição
        prescricao_serializer = PrescricaoSerializer(data=prescricao_data)
        if prescricao_serializer.is_valid():
            prescricao_serializer.save()
            return Response(prescricao_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(prescricao_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ViewSet de Medicamentos
class MedicamentoViewSet(viewsets.ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer

# ViewSet de Usuários
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# ViewSet de Registros
class RegistroViewSet(viewsets.ModelViewSet):
    queryset = Registro.objects.all()
    serializer_class = RegistroSerializer