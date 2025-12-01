from rest_framework import serializers
from apps.practicantes.domain.practicante import Practicante, EstadoPracticante

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

class AsistenciaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    practicante_id = serializers.IntegerField()
    fecha = serializers.DateField()
    hora_entrada = serializers.TimeField()
    hora_salida = serializers.TimeField(required=False, allow_null=True)

class HorarioSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    practicante_id = serializers.IntegerField()
    dia_semana = serializers.CharField(max_length=10)
    hora_inicio = serializers.TimeField()
    hora_fin = serializers.TimeField()

class CalendarioSemanalSerializer(serializers.Serializer):
    fecha = serializers.DateField()
    dia_semana = serializers.CharField()
    trabajó = serializers.BooleanField()
    horas_trabajadas = serializers.FloatField()

class EstadisticasPersonalesSerializer(serializers.Serializer):
    semana_actual = serializers.DictField()
    dias_trabajados = serializers.IntegerField()
    dias_con_asistencia_completa = serializers.IntegerField()
    total_horas_semana = serializers.FloatField()
    promedio_horas_diario = serializers.FloatField()
    dias_semana_total = serializers.IntegerField()

class AdvertenciaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    practicante_id = serializers.IntegerField()
    tipo = serializers.CharField()
    gravedad = serializers.CharField()
    descripcion = serializers.CharField()
    fecha = serializers.DateField()
    resuelta = serializers.BooleanField()
    fecha_resolucion = serializers.DateField(required=False, allow_null=True)

class AdvertenciaStatsSerializer(serializers.Serializer):
    total = serializers.IntegerField()
    leves = serializers.IntegerField()
    moderadas = serializers.IntegerField()
    graves = serializers.IntegerField()
    resueltas = serializers.IntegerField()
    pendientes = serializers.IntegerField()
