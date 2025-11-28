from typing import List, Optional, Tuple
from datetime import datetime
from django.db.models import Count, Q

from apps.practicantes.domain.historial import (
    AccionPracticante,
    ResumenPracticante,
    EstadisticasHistorial,
    TipoAccion,
    EstadoPracticante,
    FiltrosHistorial
)
from apps.practicantes.domain.repositories import HistorialRepository
from apps.practicantes.infrastructure.models import (
    AccionPracticante as AccionPracticanteModel,
    Practicante as PracticanteModel
)


class DjangoORMHistorialRepository(HistorialRepository):
    """
    Implementación del repositorio de historial utilizando Django ORM.
    Gestiona las operaciones de base de datos para el historial de acciones de practicantes.
    """

    def obtener_estadisticas(self) -> EstadisticasHistorial:
        """
        Obtiene las estadísticas generales del historial.
        
        Returns:
            EstadisticasHistorial: Objeto con las estadísticas del historial
        """
        # Obtener conteos de cada tipo de acción
        stats = AccionPracticanteModel.objects.aggregate(
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

    def obtener_historial_detallado(
        self,
        filtros: FiltrosHistorial,
        pagina: int = 1,
        por_pagina: int = 10
    ) -> Tuple[List[AccionPracticante], int]:
        """
        Obtiene el historial detallado con paginación y filtros.
        
        Args:
            filtros: Filtros a aplicar
            pagina: Número de página
            por_pagina: Elementos por página
            
        Returns:
            Tuple con la lista de acciones y el total de registros
        """
        queryset = AccionPracticanteModel.objects.all()
        
        # Aplicar filtros
        if filtros.busqueda:
            queryset = queryset.filter(
                Q(descripcion__icontains=filtros.busqueda) |
                Q(detalles__icontains=filtros.busqueda)
            )
            
        if filtros.area:
            queryset = queryset.filter(area=filtros.area)
            
        if filtros.tipo_accion:
            queryset = queryset.filter(tipo_accion=filtros.tipo_accion)
            
        if filtros.estado_final:
            queryset = queryset.filter(estado_final=filtros.estado_final)
            
        if filtros.fecha_desde:
            queryset = queryset.filter(fecha__gte=filtros.fecha_desde)
            
        if filtros.fecha_hasta:
            # Añadir un día para incluir el día completo
            hasta = filtros.fecha_hasta.replace(hour=23, minute=59, second=59)
            queryset = queryset.filter(fecha__lte=hasta)
        
        # Contar total antes de paginar
        total = queryset.count()
        
        # Aplicar paginación
        inicio = (pagina - 1) * por_pagina
        fin = inicio + por_pagina
        acciones = queryset.order_by('-fecha')[inicio:fin]
        
        # Convertir a objetos de dominio
        acciones_dominio = [
            AccionPracticante(
                id=accion.id,
                fecha=accion.fecha,
                practicante_id=accion.practicante_id,
                tipo_accion=accion.tipo_accion,
                descripcion=accion.descripcion,
                usuario=accion.usuario,
                detalles=accion.detalles,
                area=accion.area,
                estado_final=accion.estado_final
            )
            for accion in acciones
        ]
        
        return acciones_dominio, total

    def contar_historial_detallado(self, filtros: FiltrosHistorial) -> int:
        """
        Cuenta el total de registros que coinciden con los filtros.
        
        Args:
            filtros: Filtros a aplicar
            
        Returns:
            Número total de registros
        """
        queryset = AccionPracticanteModel.objects.all()
        
        # Aplicar los mismos filtros que en obtener_historial_detallado
        if filtros.busqueda:
            queryset = queryset.filter(
                Q(descripcion__icontains=filtros.busqueda) |
                Q(detalles__icontains=filtros.busqueda)
            )
            
        if filtros.area:
            queryset = queryset.filter(area=filtros.area)
            
        if filtros.tipo_accion:
            queryset = queryset.filter(tipo_accion=filtros.tipo_accion)
            
        if filtros.estado_final:
            queryset = queryset.filter(estado_final=filtros.estado_final)
            
        if filtros.fecha_desde:
            queryset = queryset.filter(fecha__gte=filtros.fecha_desde)
            
        if filtros.fecha_hasta:
            hasta = filtros.fecha_hasta.replace(hour=23, minute=59, second=59)
            queryset = queryset.filter(fecha__lte=hasta)
        
        return queryset.count()

    def obtener_resumen_practicantes(
        self,
        filtros: FiltrosHistorial
    ) -> List[ResumenPracticante]:
        """
        Obtiene un resumen de los practicantes con sus estadísticas.
        
        Args:
            filtros: Filtros a aplicar
            
        Returns:
            Lista de resúmenes de practicantes
        """
        # Implementación simplificada - ajustar según necesidades
        practicantes = PracticanteModel.objects.all()
        
        if filtros.area:
            practicantes = practicantes.filter(area=filtros.area)
            
        if filtros.estado_final:
            practicantes = practicantes.filter(estado=filtros.estado_final)
        
        resumenes = []
        for p in practicantes:
            acciones = AccionPracticanteModel.objects.filter(practicante_id=p.id)
            
            resumen = ResumenPracticante(
                id=p.id,
                nombre_completo=f"{p.nombre} {p.apellido}",
                area=p.area,
                estado=p.estado,
                ultima_accion=acciones.order_by('-fecha').first().descripcion if acciones.exists() else "Sin acciones",
                en_sistema=True,  # Asumimos que está en el sistema si existe
                total_advertencias=acciones.filter(tipo_accion=TipoAccion.ADVERTENCIA).count(),
                total_traslados=acciones.filter(tipo_accion=TipoAccion.TRASLADO).count(),
                total_expulsiones=acciones.filter(tipo_accion=TipoAccion.EXPULSION).count()
            )
            resumenes.append(resumen)
            
        return resumenes

    def obtener_practicante_por_id(self, practicante_id: int) -> Optional[ResumenPracticante]:
        """
        Obtiene el resumen de un practicante por su ID.
        
        Args:
            practicante_id: ID del practicante
            
        Returns:
            Resumen del practicante o None si no se encuentra
        """
        try:
            p = PracticanteModel.objects.get(id=practicante_id)
            acciones = AccionPracticanteModel.objects.filter(practicante_id=p.id)
            
            return ResumenPracticante(
                id=p.id,
                nombre_completo=f"{p.nombre} {p.apellido}",
                area=p.area,
                estado=p.estado,
                ultima_accion=acciones.order_by('-fecha').first().descripcion if acciones.exists() else "Sin acciones",
                en_sistema=True,
                total_advertencias=acciones.filter(tipo_accion=TipoAccion.ADVERTENCIA).count(),
                total_traslados=acciones.filter(tipo_accion=TipoAccion.TRASLADO).count(),
                total_expulsiones=acciones.filter(tipo_accion=TipoAccion.EXPULSION).count()
            )
        except PracticanteModel.DoesNotExist:
            return None

    def crear_accion(
        self,
        practicante_id: int,
        tipo: TipoAccion,
        descripcion: str,
        usuario: str,
        detalles: dict,
        area: str = None,
        estado_final: EstadoPracticante = None
    ) -> AccionPracticante:
        """
        Crea una nueva acción en el historial.
        
        Args:
            practicante_id: ID del practicante
            tipo: Tipo de acción
            descripcion: Descripción de la acción
            usuario: Usuario que realiza la acción
            detalles: Detalles adicionales
            area: Área relacionada (opcional)
            estado_final: Estado final del practicante (opcional)
            
        Returns:
            La acción creada
        """
        accion = AccionPracticanteModel.objects.create(
            practicante_id=practicante_id,
            tipo_accion=tipo,
            descripcion=descripcion,
            usuario=usuario,
            detalles=detalles,
            area=area,
            estado_final=estado_final,
            fecha=datetime.now()
        )
        
        return AccionPracticante(
            id=accion.id,
            fecha=accion.fecha,
            practicante_id=accion.practicante_id,
            tipo_accion=accion.tipo_accion,
            descripcion=accion.descripcion,
            usuario=accion.usuario,
            detalles=accion.detalles,
            area=accion.area,
            estado_final=accion.estado_final
        )

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
