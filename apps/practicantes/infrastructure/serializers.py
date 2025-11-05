from rest_framework import serializers
from apps.practicantes.domain.models import Practicante

# Serializer para el modelo Practicante
class PracticanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Practicante
        fields = '__all__'

# Serializer para las estadísticas de practicantes
class EstadisticasSerializer(serializers.Serializer):
    total = serializers.IntegerField()
    activos = serializers.IntegerField()
    en_recuperacion = serializers.IntegerField()
    en_riesgo = serializers.IntegerField()
