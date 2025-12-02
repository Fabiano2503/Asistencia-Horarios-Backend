from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action, api_view # Importamos api_view y Response
from .serializers import PracticanteSerializer, EstadisticasSerializer
from ..application.services import PracticanteService
from .django_orm_repository import DjangoPracticanteRepository
from django.http import HttpResponse # Necesario para las exportaciones (ej: CSV, Excel)

# Para usar las vistas de función simples
from rest_framework.decorators import api_view # <-- Asegúrate de tener esto

# ViewSet para gestionar las operaciones CRUD y estadísticas de practicantes
class PracticanteViewSet(viewsets.GenericViewSet):
    # ... (Todo tu código CRUD, retrieve, create, update, destroy, estadisticas, etc. VA AQUÍ) ...
    serializer_class = PracticanteSerializer

    def get_service(self) -> PracticanteService:
        return PracticanteService(DjangoPracticanteRepository())

    # Listado con filtros y paginación
    def list(self, request, *args, **kwargs):
        # ... Tu código list aquí ...
        service = self.get_service()
        # ... (código para filtrar y paginar) ...
        practicantes = service.filter_practicantes(None, None, None) # Placeholder
        serializer = self.get_serializer(practicantes, many=True)
        return Response(serializer.data)

    # ... (Resto de las funciones CRUD: retrieve, create, update, partial_update, destroy) ...

    # Acción personalizada para estadísticas
    @action(detail=False, methods=['get'])
    def estadisticas(self, request):
        service = self.get_service()
        stats = service.get_practicante_stats()
        serializer = EstadisticasSerializer(stats)
        return Response(serializer.data)

# -----------------------------------------------------------
# VISTAS DE FUNCIÓN REQUERIDAS POR apps/practicantes/infrastructure/urls.py
# -----------------------------------------------------------

# Vistas para Reportes y Permisos (Usan el decorador @api_view)

@api_view(['GET'])
def advertencias_mes_actual(request):
    """Lógica para la ruta advertencias/mes/"""
    service = PracticanteService(DjangoPracticanteRepository())
    data = service.get_advertencias_mes_actual()
    return Response(data, status=status.HTTP_200_OK)

@api_view(['GET'])
def advertencias_historico(request):
    """Lógica para la ruta advertencias/historico/"""
    service = PracticanteService(DjangoPracticanteRepository())
    data = service.get_advertencias_historico()
    return Response(data, status=status.HTTP_200_OK)

@api_view(['GET'])
def permisos_semana_actual(request):
    """Lógica para la ruta permisos/semana/"""
    service = PracticanteService(DjangoPracticanteRepository())
    data = service.get_permisos_semana_actual()
    return Response(data, status=status.HTTP_200_OK)

@api_view(['GET'])
def permisos_por_practicante(request):
    """Lógica para la ruta permisos/practicante/"""
    service = PracticanteService(DjangoPracticanteRepository())
    data = service.get_permisos_por_practicante()
    return Response(data, status=status.HTTP_200_OK)

# Las funciones de exportación suelen devolver un HttpResponse, no un Response de DRF
def export_reporte_semanal(request):
    """Lógica para la ruta exportar/semanal/"""
    service = PracticanteService(DjangoPracticanteRepository())
    # ⚠️ Esta función debe generar el archivo (CSV/Excel) y devolverlo en un HttpResponse
    return HttpResponse("Generando reporte semanal...", status=status.HTTP_200_OK)

def export_reporte_mensual(request):
    """Lógica para la ruta exportar/mensual/"""
    service = PracticanteService(DjangoPracticanteRepository())
    # ⚠️ Esta función debe generar el archivo (CSV/Excel) y devolverlo en un HttpResponse
    return HttpResponse("Generando reporte mensual...", status=status.HTTP_200_OK)
