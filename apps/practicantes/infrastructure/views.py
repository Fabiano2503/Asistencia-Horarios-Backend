from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import (
    PracticanteSerializer, 
    EstadisticasSerializer,
    ReforzamientoSerializer,
    ActualizarAreaMotivoSerializer,
    MetricasReforzamientoSerializer
)
from ..application.services import PracticanteService, ReforzamientoService
from .django_orm_repository import DjangoPracticanteRepository, DjangoReforzamientoRepository

# ViewSet para gestionar las operaciones CRUD y estadísticas de practicantes
class PracticanteViewSet(viewsets.GenericViewSet):
    serializer_class = PracticanteSerializer

    def get_service(self) -> PracticanteService:
        return PracticanteService(
            DjangoPracticanteRepository(),
            DjangoReforzamientoRepository()
        )

    # Listado con filtros y paginación
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

    # Obtener un solo practicante
    def retrieve(self, request, pk=None):
        service = self.get_service()
        practicante = service.get_practicante_by_id(pk)
        if not practicante:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(practicante)
        return Response(serializer.data)

    # Crear un practicante
    def create(self, request):
        service = self.get_service()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        practicante = service.create_practicante(serializer.validated_data)
        serializer = self.get_serializer(practicante)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # Actualizar un practicante
    def update(self, request, pk=None):
        service = self.get_service()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        practicante = service.update_practicante(pk, serializer.validated_data)
        if not practicante:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(practicante)
        return Response(serializer.data)

    # Actualización parcial (PATCH)
    def partial_update(self, request, pk=None):
        service = self.get_service()
        serializer = self.get_serializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        practicante = service.update_practicante(pk, serializer.validated_data)
        if not practicante:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(practicante)
        return Response(serializer.data)

    # Eliminar un practicante
    def destroy(self, request, pk=None):
        service = self.get_service()
        service.delete_practicante(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

    # Acción personalizada para estadísticas
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
        
        if not reforzamiento:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.get_serializer(reforzamiento)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def reintegrar(self, request, pk=None):
        service = self.get_service()
        reforzamiento = service.marcar_como_reintegrado(pk)
        
        if not reforzamiento:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.get_serializer(reforzamiento)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def metricas(self, request):
        service = self.get_service()
        metricas = service.get_metricas()
        serializer = MetricasReforzamientoSerializer(metricas)
        return Response(serializer.data)