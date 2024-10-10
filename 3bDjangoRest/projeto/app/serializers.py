from rest_framework import serializers
from .models import Usuario, Medicamento, Prescricao, Registro

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        
class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = '__all__'
                
class PrescricaoSerializer(serializers.ModelSerializer):
    paciente = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all())
    medicamento = serializers.PrimaryKeyRelatedField(queryset=Medicamento.objects.all())
    
    class Meta:
        model = Prescricao
        fields = '__all__'

class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registro
        fields = '__all__'