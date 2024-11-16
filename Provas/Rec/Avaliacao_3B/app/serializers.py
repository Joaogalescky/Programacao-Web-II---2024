from rest_framework import serializers
from .models import Treino, Exercicio


class ExercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercicio
        fields = '__all__'

class TreinoSerializer(serializers.ModelSerializer):
    exercicios = serializers.PrimaryKeyRelatedField(queryset=Exercicio.objects.all(), many=True) # Retornar objetos completos

    class Meta:
        model = Treino
        fields = '__all__'

    def create(self, validated_data):
        exercicios_data = validated_data.pop('exercicios', [])
        treino = Treino.objects.create(**validated_data)
        treino.exercicios.set(exercicios_data)
        return treino

    def update(self, instance, validated_data):
        exercicios_data = validated_data.pop('exercicios', [])
        instance.data_inicio = validated_data.get('data_inicio', instance.data_inicio)
        instance.data_fim = validated_data.get('data_fim', instance.data_fim)
        instance.objetivo = validated_data.get('objetivo', instance.objetivo)
        instance.save()
        instance.exercicios.set(exercicios_data)
        return instance
