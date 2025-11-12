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
7. Agregar en: apps/practicantes/infrastructure/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import (
    PracticanteSerializer, 
    EstadisticasSerializer,
    ReforzamientoSerializer,  # NUEVO
    ActualizarAreaMotivoSerializer,  # NUEVO
    MetricasReforzamientoSerializer  # NUEVO
)
from ..application.services import PracticanteService, ReforzamientoService  # ACTUALIZADO
from .django_orm_repository import DjangoPracticanteRepository, DjangoReforzamientoRepository  # ACTUALIZADO

# ViewSet para gestionar las operaciones CRUD y estadísticas de practicantes
class PracticanteViewSet(viewsets.GenericViewSet):
    serializer_class = PracticanteSerializer

    def get_service(self) -> PracticanteService:
        return PracticanteService(DjangoPracticanteRepository())

    def list(self, request, *args, **kwargs):
        service = self.get_service()
        nombre = request.query_params.get('nombre')
        correo = request.query_params.get('correo')
        estado = request.query_params.get('estado')

        practicantes = service.filter_practicantes(nombre, correo, estado)

        page = self.paginate_queryset(practicantes)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(practicantes, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        service = self.get_service()
        practicante = service.get_practicante_by_id(pk)
        if not practicante:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(practicante)
        return Response(serializer.data)

    def create(self, request):
        service = self.get_service()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        practicante = service.create_practicante(serializer.validated_data)
        serializer = self.get_serializer(practicante)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        service = self.get_service()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        practicante = service.update_practicante(pk, serializer.validated_data)
        if not practicante:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(practicante)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        service = self.get_service()
        serializer = self.get_serializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        practicante = service.update_practicante(pk, serializer.validated_data)
        if not practicante:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(practicante)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        service = self.get_service()
        service.delete_practicante(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['get'])
    def estadisticas(self, request):
        service = self.get_service()
        stats = service.get_practicante_stats()
        serializer = EstadisticasSerializer(stats)
        return Response(serializer.data)


# ViewSet para gestionar reforzamiento
class ReforzamientoViewSet(viewsets.GenericViewSet):
    serializer_class = ReforzamientoSerializer

    def get_service(self) -> ReforzamientoService:
        return ReforzamientoService(
            DjangoReforzamientoRepository(),
            DjangoPracticanteRepository()
        )

    def list(self, request, *args, **kwargs):
        service = self.get_service()
        estado = request.query_params.get('estado')
        
        if estado:
            reforzamientos = service.filter_by_estado(estado)
        else:
            reforzamientos = service.get_all_reforzamientos()

        page = self.paginate_queryset(reforzamientos)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(reforzamientos, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        service = self.get_service()
        reforzamiento = service.get_reforzamiento_by_id(pk)
        if not reforzamiento:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(reforzamiento)
        return Response(serializer.data)

    def create(self, request):
        service = self.get_service()
        practicante_id = request.data.get('practicante_id')
        
        if not practicante_id:
            return Response(
                {'detail': 'practicante_id es requerido'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        reforzamiento = service.crear_reforzamiento_desde_practicante(practicante_id)
        
        if not reforzamiento:
            return Response(
                {'detail': 'No se pudo crear el reforzamiento. Verifica que el practicante exista y esté en estado de recuperación.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = self.get_serializer(reforzamiento)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['patch'])
    def actualizar_info(self, request, pk=None):
        service = self.get_service()
        serializer = ActualizarAreaMotivoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        area = serializer.validated_data.get('area')
        motivo = serializer.validated_data.get('motivo')
        
        reforzamiento = service.actualizar_area_motivo(pk, area, motivo)
        
        if not reforzamiento:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        response_serializer = self.get_serializer(reforzamiento)
        return Response(response_serializer.data)

    @action(detail=True, methods=['post'])
    def completar(self, request, pk=None):
        service = self.get_service()
        reforzamiento = service.marcar_como_completado(pk)
        
        if not reforzamiento