from rest_framework import serializers
from apps.practicantes.domain.practicante import Practicante, EstadoPracticante
from apps.practicantes.domain.reforzamiento import PracticanteReforzamiento, EstadoReforzamiento

# Serializer para entidades de dominio Practicante
class PracticanteSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    id_discord = serializers.IntegerField()
    nombre = serializers.CharField(max_length=100)
    apellido = serializers.CharField(max_length=100)
    correo = serializers.EmailField()
    semestre = serializers.IntegerField()
    estado = serializers.ChoiceField(choices=[e.value for e in EstadoPracticante])

    def create(self, validated_data):
        # Convertir validated_data a entidad de dominio
        return Practicante(**validated_data)

    def update(self, instance: Practicante, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        return instance

# Serializer para las estadísticas de practicantes
class EstadisticasSerializer(serializers.Serializer):
    total = serializers.IntegerField()
    activos = serializers.IntegerField()
    en_recuperacion = serializers.IntegerField()
    en_riesgo = serializers.IntegerField()

# Serializer para Reforzamiento
class ReforzamientoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    practicante_id = serializers.IntegerField(read_only=True)
    nombre_completo = serializers.CharField(read_only=True)
    area = serializers.CharField(max_length=100)
    motivo = serializers.CharField()
    fecha_ingreso = serializers.DateTimeField(read_only=True)
    estado = serializers.ChoiceField(
        choices=[e.value for e in EstadoReforzamiento],
        read_only=True
    )

    def create(self, validated_data):
        return PracticanteReforzamiento(**validated_data)

    def update(self, instance: PracticanteReforzamiento, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        return instance

# Serializer para actualizar solo área y motivo
class ActualizarAreaMotivoSerializer(serializers.Serializer):
    area = serializers.CharField(max_length=100, required=False, allow_blank=True)
    motivo = serializers.CharField(required=False, allow_blank=True)


# Serializer para métricas de reforzamiento
class MetricasReforzamientoSerializer(serializers.Serializer):
    en_reforzamiento = serializers.IntegerField()
    completados = serializers.IntegerField()
    reintegrados = serializers.IntegerField()