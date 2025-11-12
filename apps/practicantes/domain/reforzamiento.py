from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from enum import Enum

class EstadoReforzamiento(Enum):
    EN_REFORZAMIENTO = "en_reforzamiento"
    COMPLETADO = "completado"
    REINTEGRADO = "reintegrado"

@dataclass
class PracticanteReforzamiento:
    practicante_id: int
    nombre_completo: str
    area: str
    motivo: str
    fecha_ingreso: datetime
    estado: EstadoReforzamiento = EstadoReforzamiento.EN_REFORZAMIENTO
    id: Optional[int] = None

    def __post_init__(self):
        if not self.area or self.area.strip() == "":
            self.area = "Falta agregar"
        if not self.motivo or self.motivo.strip() == "":
            self.motivo = "Falta agregar"

    def actualizar_informacion(self, area: Optional[str] = None, motivo: Optional[str] = None):
        if area is not None:
            self.area = area if area.strip() != "" else "Falta agregar"
        if motivo is not None:
            self.motivo = motivo if motivo.strip() != "" else "Falta agregar"

    def marcar_completado(self):
        self.estado = EstadoReforzamiento.COMPLETADO

    def marcar_reintegrado(self):
        self.estado = EstadoReforzamiento.REINTEGRADO

    def __str__(self):
        return f"{self.nombre_completo} - {self.area} - {self.estado.value}"
