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
    total_registros: int
    total_advertencias: int
    total_traslados: int
    total_expulsiones: int
    total_practicantes: int
    total_activos: int
    total_trasladados: int
    total_expulsados: int
    total_en_reforzamiento: int

@dataclass
class FiltrosHistorial:
    busqueda: Optional[str] = None
    area: Optional[str] = None
    tipo_accion: Optional[TipoAccion] = None
    estado_final: Optional[EstadoPracticante] = None
    fecha_desde: Optional[datetime] = None
    fecha_hasta: Optional[datetime] = None
