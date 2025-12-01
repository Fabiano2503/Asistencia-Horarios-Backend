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
    def obtener_estadisticas(self, fecha_desde: Optional[datetime] = None, fecha_hasta: Optional[datetime] = None) -> EstadisticasHistorial:
        """
        Obtiene estadísticas generales del historial de practicantes
        
        Args:
            fecha_desde: Fecha desde la cual obtener estadísticas
            fecha_hasta: Fecha hasta la cual obtener estadísticas
            
        Returns:
            EstadisticasHistorial: Objeto con las estadísticas
        """
        pass

    @abstractmethod
    def obtener_historial(
        self,
        busqueda: Optional[str] = None,
        area: Optional[str] = None,
        tipo_accion: Optional[TipoAccion] = None,
        estado: Optional[EstadoPracticante] = None,
        fecha_desde: Optional[datetime] = None,
        fecha_hasta: Optional[datetime] = None,
        orden: str = '-fecha_accion'
    ) -> List[AccionPracticante]:
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
        pass

    @abstractmethod
    def registrar_accion(
        self,
        practicante_id: int,
        tipo_accion: TipoAccion,
        descripcion: str,
        usuario_id: int,
        detalles: Dict[str, Any]
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
