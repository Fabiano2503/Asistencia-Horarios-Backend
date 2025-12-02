from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import PracticanteSerializer, EstadisticasSerializer
# Importa otros serializers si son necesarios para las advertencias
# from .serializers import AdvertenciaSerializer # <--- Descomentar si usas un serializer específico

from ..application.services import PracticanteService
from .django_orm_repository import DjangoPracticanteRepository

# ViewSet para gestionar las operaciones CRUD y estadísticas de practicantes
class PracticanteViewSet(viewsets.GenericViewSet):
    """
    ViewSet para manejar las operaciones CRUD y acciones personalizadas
    relacionadas con el modelo Practicante.
    """
    serializer_class = PracticanteSerializer

    def get_service(self) -> PracticanteService:
        """Devuelve una instancia del servicio de aplicación."""
        return PracticanteService(DjangoPracticanteRepository())

    # --- Operaciones CRUD (Heredadas de GenericViewSet) ---

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

    # Actualizar un practicante (PUT)
    def update(self, request, pk=None):
        service = self.get_service()
        # Nota: La validación del serializer debe hacerse con el objeto existente si no estás usando 'instance'
        # Pero mantendremos tu flujo actual por simplicidad, asumiendo que el Service maneja la instancia.
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

    # --- Acciones Personalizadas (@action) ---
    
    # Acción para obtener estadísticas generales (ya la tenías)
    @action(detail=False, methods=['get'])
    def estadisticas(self, request):
        service = self.get_service()
        stats = service.get_practicante_stats()
        serializer = EstadisticasSerializer(stats)
        return Response(serializer.data)

    # SOLUCIÓN AL BUG: Implementación de la función faltante
    # URL generada por el router: /api/practicantes/advertencias_mes_actual/
    @action(detail=False, methods=['get'])
    def advertencias_mes_actual(self, request):
        """
        Obtiene el listado de advertencias para todos los practicantes 
        en el mes actual.
        """
        service = self.get_service()
        
        # ⚠️ Necesitarás crear este método en PracticanteService
        advertencias = service.get_advertencias_mes_actual() 
        
        # ⚠️ Usa un serializer apropiado para las advertencias si es necesario
        # serializer = AdvertenciaSerializer(advertencias, many=True) 
        
        # Si el Service devuelve la data ya lista (ej. un diccionario o lista simple):
        return Response(advertencias, status=status.HTTP_200_OK)
