from rest_framework import serializers
from src.domain.entities.horario import Horario

class HorarioSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    practicante_id = serializers.IntegerField()
    servidor_id = serializers.IntegerField()
    dia = serializers.CharField()
    hora_inicio = serializers.TimeField()
    hora_fin = serializers.TimeField()
    estado = serializers.CharField(read_only=True)

    def create(self, validated_data):
        return Horario(**validated_data)