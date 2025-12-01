from typing import List, Optional, Dict, Any
from datetime import datetime
from django.db.models import Count, Q

from apps.practicantes.domain.historial import (
    AccionPracticante as AccionPracticanteDomain,
    EstadisticasHistorial,
    TipoAccion,
    EstadoPracticante
)
from apps.practicantes.domain.repositories import HistorialRepository
from apps.practicantes.infrastructure.models import (
    AccionPracticante,
    Practicante as PracticanteModel
)


class DjangoORMHistorialRepository(HistorialRepository):
    """
    Implementación del repositorio de historial utilizando Django ORM.
    Gestiona las operaciones de base de datos para el historial de acciones de practicantes.
    """

    def obtener_estadisticas(
        self, 
        fecha_desde: Optional[datetime] = None, 
        fecha_hasta: Optional[datetime] = None
    ) -> EstadisticasHistorial:
        """
        Obtiene las estadísticas generales del historial.
        
        Args:
            fecha_desde: Fecha desde la cual obtener estadísticas
            fecha_hasta: Fecha hasta la cual obtener estadísticas
            
        Returns:
            EstadisticasHistorial: Objeto con las estadísticas del historial
        """
        # Crear filtros base
        filters = Q()
        if fecha_desde:
            filters &= Q(fecha_accion__gte=fecha_desde)
        if fecha_hasta:
            # Añadir un día para incluir el día completo
            hasta = fecha_hasta.replace(hour=23, minute=59, second=59)
            filters &= Q(fecha_accion__lte=hasta)
        
        # Obtener conteos de cada tipo de acción
        queryset = AccionPracticanteModel.objects.filter(filters)
        
        stats = queryset.aggregate(
            total_registros=Count('id'),
            total_advertencias=Count('id', filter=Q(tipo_accion=TipoAccion.ADVERTENCIA)),
            total_traslados=Count('id', filter=Q(tipo_accion=TipoAccion.TRASLADO)),
            total_expulsiones=Count('id', filter=Q(tipo_accion=TipoAccion.EXPULSION))
        )
        
        return EstadisticasHistorial(
            total_registros=stats['total_registros'],
            total_advertencias=stats['total_advertencias'],
            total_traslados=stats['total_traslados'],
            total_expulsiones=stats['total_expulsiones']
        )

    def obtener_historial(
        self,
        busqueda: Optional[str] = None,
        area: Optional[str] = None,
        tipo_accion: Optional[TipoAccion] = None,
        estado: Optional[EstadoPracticante] = None,
        fecha_desde: Optional[datetime] = None,
        fecha_hasta: Optional[datetime] = None,
        orden: str = '-fecha_accion'
    ) -> List[AccionPracticanteDomain]:
        """
        Obtiene el historial de acciones con filtros opcionales.
        
        Args:
            busqueda: Término de búsqueda para filtrar por nombre o apellido del practicante
            area: Área para filtrar las acciones
            tipo_accion: Tipo de acción a filtrar
            estado: Estado del practicante a filtrar
            fecha_desde: Fecha mínima de las acciones
            fecha_hasta: Fecha máxima de las acciones
            orden: Campo por el que ordenar los resultados (prefijo '-' para orden descendente)
            
        Returns:
            Lista de acciones de historial que coinciden con los filtros
        """
        queryset = AccionPracticanteModel.objects.all()
        
        # Aplicar filtros
        if busqueda:
            queryset = queryset.filter(
                Q(practicante__nombre__icontains=busqueda) |
                Q(practicante__apellido__icontains=busqueda) |
                Q(descripcion__icontains=busqueda)
            )
            
        if area:
            queryset = queryset.filter(area=area)
            
        if tipo_accion:
            queryset = queryset.filter(tipo_accion=tipo_accion)
            
        if estado:
            queryset = queryset.filter(estado=estado)
            
        if fecha_desde:
            queryset = queryset.filter(fecha_accion__gte=fecha_desde)
            
        if fecha_hasta:
            # Añadir un día para incluir el día completo
            hasta = fecha_hasta.replace(hour=23, minute=59, second=59)
            queryset = queryset.filter(fecha_accion__lte=hasta)
        
        # Aplicar ordenación
        queryset = queryset.order_by(orden)
        
        # Convertir a objetos de dominio
        return [
            self._to_domain(accion_db) 
            for accion_db in queryset.select_related('practicante')
        ]

    def registrar_accion(
        self,
        practicante_id: int,
        tipo_accion: TipoAccion,
        descripcion: str,
        usuario_id: int,
        detalles: Dict[str, Any]
    ) -> AccionPracticanteDomain:
        """
        Registra una nueva acción en el historial.
        
        Args:
            practicante_id: ID del practicante relacionado con la acción
            tipo_accion: Tipo de acción realizada
            descripcion: Descripción detallada de la acción
            usuario_id: ID del usuario que realizó la acción
            detalles: Datos adicionales sobre la acción
            
        Returns:
            La acción de historial registrada
        """
        # Obtener el practicante
        try:
            practicante = PracticanteModel.objects.get(id=practicante_id)
        except PracticanteModel.DoesNotExist:
            raise ValueError(f"No existe un practicante con ID {practicante_id}")
        
        # Crear la acción
        accion_db = AccionPracticanteModel.objects.create(
            practicante=practicante,
            tipo_accion=tipo_accion,
            descripcion=descripcion,
            usuario_id=usuario_id,
            detalles=detalles,
            area=practicante.area,
            estado=practicante.estado
        )
        
        return self._to_domain(accion_db)
    
    def actualizar_estado_practicante(
        self,
        practicante_id: int,
        nuevo_estado: EstadoPracticante
    ) -> None:
        """
        Actualiza el estado de un practicante.
        
        Args:
            practicante_id: ID del practicante
            nuevo_estado: Nuevo estado
        """
        PracticanteModel.objects.filter(id=practicante_id).update(estado=nuevo_estado)
    
    def obtener_areas(self) -> List[str]:
        """
        Obtiene la lista de áreas únicas.
        
        Returns:
            Lista de nombres de áreas únicas
        """
        return list(PracticanteModel.objects.values_list('area', flat=True).distinct())
    
    def _to_domain(self, accion_db: AccionPracticante) -> AccionPracticanteDomain:
        """
        Convierte un modelo de base de datos a un objeto de dominio.
        """
        return AccionPracticanteDomain(
            id=accion_db.id,
            practicante_id=accion_db.practicante_id,
            tipo_accion=accion_db.tipo_accion,
            descripcion=accion_db.descripcion,
            fecha_accion=accion_db.fecha_accion,
            usuario_id=accion_db.usuario_id if accion_db.usuario_id else None,
            detalles=accion_db.detalles,
            area=accion_db.area,
            estado=accion_db.estado,
            numero_advertencia=accion_db.numero_advertencia
        )
