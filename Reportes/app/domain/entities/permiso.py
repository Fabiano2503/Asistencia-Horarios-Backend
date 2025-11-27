from dataclasses import dataclass
from datetime import date

@dataclass
class Permiso:
    id: int
    practicante_id: int
    fecha_inicio: date
    fecha_fin: date
    tipo: str  # médico, personal, etc.
    aprobado: bool = True