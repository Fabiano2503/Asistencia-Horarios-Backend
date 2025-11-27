from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import PracticanteSerializer, EstadisticasSerializer, AsistenciaSerializer, HorarioSerializer, CalendarioSemanalSerializer, EstadisticasPersonalesSerializer, AdvertenciaSerializer, AdvertenciaStatsSerializer
from ..application.services import PracticanteService, AsistenciaService, HorarioService, AdvertenciaService
from .django_orm_repository import DjangoPracticanteRepository, DjangoAsistenciaRepository, DjangoHorarioRepository, DjangoAdvertenciaRepository
from rest_framework.permissions import IsAuthenticated
from functools import wraps


def validate_practicante_ownership(view_func):
    """
    Decorator que valida que el practicante solo pueda acceder a sus propios datos.
    Requiere header X-Practicante-ID con el ID del practicante autenticado.
    """
    @wraps(view_func)
    def wrapper(self, request, *args, **kwargs):
        # Obtener el ID del practicante autenticado desde el header
        authenticated_practicante_id = request.headers.get('X-Practicante-ID')

        if not authenticated_practicante_id:
            return Response(
                {"error": "Se requiere header X-Practicante-ID para autenticación"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        # Obtener el ID solicitado desde el query parameter
        requested_practicante_id = request.query_params.get('practicante_id')

        if not requested_practicante_id:
            # Si no hay query param, usar el del header como default
            requested_practicante_id = authenticated_practicante_id

        # Validar que coincidan
        if str(authenticated_practicante_id) != str(requested_practicante_id):
            return Response(
                {"error": "No tienes permisos para acceder a estos datos"},
                status=status.HTTP_403_FORBIDDEN
            )

        # Agregar el ID validado a la request para uso posterior
        request.validated_practicante_id = int(authenticated_practicante_id)
        return view_func(self, request, *args, **kwargs)

    return wrapper

# ViewSet para gestionar las operaciones CRUD y estadísticas de practicantes
class PracticanteViewSet(viewsets.GenericViewSet):
    serializer_class = PracticanteSerializer

    def get_service(self) -> PracticanteService:
        return PracticanteService(DjangoPracticanteRepository())

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


class AsistenciaViewSet(viewsets.ViewSet):
    serializer_class = AsistenciaSerializer

    def get_service(self):
        return AsistenciaService(DjangoAsistenciaRepository())

    @validate_practicante_ownership
    def list(self, request, practicante_pk=None):
        service = self.get_service()
        practicante_id = request.validated_practicante_id
        asistencias = service.get_asistencias_by_practicante(practicante_id)
        serializer = self.serializer_class(asistencias, many=True)
        return Response(serializer.data)

    @validate_practicante_ownership
    def create(self, request, practicante_pk=None):
        service = self.get_service()
        data = request.data.copy()
        data['practicante_id'] = request.validated_practicante_id
        asistencia = service.crear_asistencia(data)
        serializer = self.serializer_class(asistencia)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class HorarioViewSet(viewsets.ViewSet):
    serializer_class = HorarioSerializer

    def get_service(self):
        return HorarioService(DjangoHorarioRepository())

    @validate_practicante_ownership
    def list(self, request, practicante_pk=None):
        service = self.get_service()
        practicante_id = request.validated_practicante_id
        horarios = service.get_horarios_by_practicante(practicante_id)
        serializer = self.serializer_class(horarios, many=True)
        return Response(serializer.data)

    @validate_practicante_ownership
    def create(self, request, practicante_pk=None):
        service = self.get_service()
        data = request.data.copy()
        data['practicante_id'] = request.validated_practicante_id
        horario = service.crear_horario(data)
        serializer = self.serializer_class(horario)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class InicioViewSet(viewsets.ViewSet):
    def list(self, request):
        # Para pruebas, usar parámetro o valor por defecto
        practicante_id = request.query_params.get('practicante_id', 1)
        return Response({
            "mensaje": "Bienvenido/a - Inicio Práctica",
            "practicante_id": practicante_id
        })

class CalendarioSemanalViewSet(viewsets.ViewSet):
    @validate_practicante_ownership
    def list(self, request):
        practicante_id = request.validated_practicante_id
        service = AsistenciaService(DjangoAsistenciaRepository())
        calendario = service.get_calendario_semanal(practicante_id)
        return Response(calendario)

class EstadisticasPersonalesViewSet(viewsets.ViewSet):
    @validate_practicante_ownership
    def list(self, request):
        practicante_id = request.validated_practicante_id
        service = AsistenciaService(DjangoAsistenciaRepository())
        estadisticas = service.get_estadisticas_personales(practicante_id)
        return Response(estadisticas)

class AdvertenciaViewSet(viewsets.ViewSet):
    serializer_class = AdvertenciaSerializer

    def get_service(self):
        return AdvertenciaService(DjangoAdvertenciaRepository())

    @validate_practicante_ownership
    def list(self, request):
        practicante_id = request.validated_practicante_id
        service = self.get_service()
        advertencias = service.get_advertencias_by_practicante(practicante_id)
        serializer = self.serializer_class(advertencias, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    @validate_practicante_ownership
    def estadisticas(self, request):
        practicante_id = request.validated_practicante_id
        service = self.get_service()
        stats = service.get_advertencia_stats_by_practicante(practicante_id)
        serializer = AdvertenciaStatsSerializer(stats)
        return Response(serializer.data)
