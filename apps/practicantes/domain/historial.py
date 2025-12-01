from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List, Optional, Dict, Any

class TipoAccion(str, Enum):
    ADVERTENCIA = "Advertencia"
    TRASLADO = "Traslado"
    EXPULSION = "Expulsión"

class EstadoPracticante(str, Enum):
    ACTIVO = "Activo"
    TRASLADADO = "Trasladado"
    EXPULSADO = "Expulsado"
    EN_REFORZAMIENTO = "En Reforzamiento"

@dataclass
class AccionPracticante:
    id: int
    practicante_id: int
    tipo: TipoAccion
    fecha: datetime
    motivo: str
    detalles: str
    estado: EstadoPracticante
    area: str
    numero_advertencia: Optional[int] = None

@dataclass
class ResumenPracticante:
    id: int
    nombre_completo: str
    email: str
    area: str
    estado: EstadoPracticante
    ultima_accion: str
    en_sistema: bool
    total_advertencias: int
    total_traslados: int
    total_expulsiones: int

@dataclass
class EstadisticasHistorial:
    """
    Estadísticas del historial de acciones de practicantes.
    
    Atributos:
        total_registros: Número total de registros en el historial
        total_advertencias: Número total de advertencias registradas
        total_traslados: Número total de traslados registrados
        total_expulsiones: Número total de expulsiones registradas
    """
    total_registros: int = 0
    total_advertencias: int = 0
    total_traslados: int = 0
    total_expulsiones: int = 0

@dataclass
class FiltrosHistorial:
    busqueda: Optional[str] = None
    area: Optional[str] = None
    tipo_accion: Optional[TipoAccion] = None
    estado_final: Optional[EstadoPracticante] = None
    fecha_desde: Optional[datetime] = None
    fecha_hasta: Optional[datetime] = None
