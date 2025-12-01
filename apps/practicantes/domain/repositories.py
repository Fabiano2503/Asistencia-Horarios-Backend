from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from datetime import datetime
from apps.practicantes.domain.practicante import Practicante
from apps.practicantes.domain.historial import (
    AccionPracticante, 
    ResumenPracticante, 
    EstadisticasHistorial,
    TipoAccion,
    EstadoPracticante,
    FiltrosHistorial
)


class PracticanteRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Practicante]:
        """Obtiene todos los practicantes"""
        pass

    @abstractmethod
    def get_by_id(self, practicante_id: int) -> Optional[Practicante]:
        """Obtiene un practicante por su ID"""
        pass

    @abstractmethod
    def create(self, practicante: Practicante) -> Practicante:
        """Crea un nuevo practicante"""
        pass

    @abstractmethod
    def update(self, practicante: Practicante) -> Practicante:
        """Actualiza un practicante existente"""
        pass

    @abstractmethod
    def delete(self, practicante_id: int) -> None:
        """Elimina un practicante por su ID"""
        pass

    @abstractmethod
    def filter(self, 
              nombre: Optional[str] = None, 
              correo: Optional[str] = None, 
              estado: Optional[str] = None) -> List[Practicante]:
        """Filtra practicantes por nombre, correo o estado"""
        pass

    @abstractmethod
    def get_stats(self) -> dict[str, int]:
        """Obtiene estadísticas generales de los practicantes"""
        pass


class HistorialRepository(ABC):
    @abstractmethod
    def obtener_estadisticas(self) -> EstadisticasHistorial:
        """
        Obtiene estadísticas generales del historial de practicantes
        
        Returns:
            EstadisticasHistorial: Objeto con las estadísticas
        """
        pass

    @abstractmethod
    def obtener_historial_detallado(
        self,
        filtros: FiltrosHistorial,
        pagina: int = 1,
        por_pagina: int = 10
    ) -> List[AccionPracticante]:
        """
        Obtiene el historial detallado de acciones con filtros
        
        Args:
            filtros: Filtros a aplicar a la búsqueda
            pagina: Número de página para la paginación
            por_pagina: Cantidad de elementos por página
            
        Returns:
            Lista de acciones de practicantes que coinciden con los filtros
        """
        pass

    @abstractmethod
    def contar_historial_detallado(self, filtros: FiltrosHistorial) -> int:
        """
        Cuenta el total de registros que coinciden con los filtros
        
        Args:
            filtros: Filtros a aplicar al conteo
            
        Returns:
            Número total de registros que coinciden con los filtros
        """
        pass

    @abstractmethod
    def obtener_resumen_practicantes(
        self,
        filtros: FiltrosHistorial
    ) -> List[ResumenPracticante]:
        """
        Obtiene un resumen de todos los practicantes con sus estadísticas
        
        Args:
            filtros: Filtros a aplicar a la búsqueda
            
        Returns:
            Lista de resúmenes de practicantes
        """
        pass

    @abstractmethod
    def obtener_practicante_por_id(self, practicante_id: int) -> Optional[ResumenPracticante]:
        """
        Obtiene el resumen de un practicante específico por su ID
        
        Args:
            practicante_id: ID del practicante a buscar
            
        Returns:
            Resumen del practicante o None si no se encuentra
        """
        pass

    @abstractmethod
    def crear_accion(
        self,
        practicante_id: int,
        tipo: TipoAccion,
        motivo: str,
        detalles: str,
        area: str,
        estado: EstadoPracticante,
        numero_advertencia: Optional[int] = None
    ) -> AccionPracticante:
        """
        Crea una nueva acción en el historial de un practicante
        
        Args:
            practicante_id: ID del practicante
            tipo: Tipo de acción
            motivo: Motivo de la acción
            detalles: Detalles adicionales
            area: Área relacionada
            estado: Estado del practicante después de la acción
            numero_advertencia: Número de advertencia (opcional)
            
        Returns:
            La acción creada
        """
        pass

    @abstractmethod
    def actualizar_estado_practicante(
        self,
        practicante_id: int,
        nuevo_estado: EstadoPracticante
    ) -> None:
        """
        Actualiza el estado de un practicante
        
        Args:
            practicante_id: ID del practicante a actualizar
            nuevo_estado: Nuevo estado del practicante
        """
        pass

    @abstractmethod
    def obtener_areas(self) -> List[str]:
        """
        Obtiene la lista de áreas únicas
        
        Returns:
            Lista de nombres de áreas únicas
        """
        pass

class AsistenciaRepository(ABC):
    @abstractmethod
    def get_by_practicante(self, practicante_id: int) -> list:
        pass
    @abstractmethod
    def create(self, asistencia) -> object:
        pass
    @abstractmethod
    def update(self, asistencia) -> object:
        pass
    @abstractmethod
    def delete(self, asistencia_id: int) -> None:
        pass

class HorarioRepository(ABC):
    @abstractmethod
    def get_by_practicante(self, practicante_id: int) -> list:
        pass
    @abstractmethod
    def create(self, horario) -> object:
        pass
    @abstractmethod
    def update(self, horario) -> object:
        pass
    @abstractmethod
    def delete(self, horario_id: int) -> None:
        pass

class AdvertenciaRepository(ABC):
    @abstractmethod
    def get_by_practicante(self, practicante_id: int) -> list:
        pass
    @abstractmethod
    def create(self, advertencia) -> object:
        pass
    @abstractmethod
    def update(self, advertencia) -> object:
        pass
    @abstractmethod
    def delete(self, advertencia_id: int) -> None:
        pass
    @abstractmethod
    def get_stats_by_practicante(self, practicante_id: int) -> dict:
        pass
