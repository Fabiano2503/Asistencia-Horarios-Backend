from dataclasses import dataclass
from datetime import date

@dataclass
class Advertencia:
    id: int
    practicante_id: int
    fecha: date
    motivo: str