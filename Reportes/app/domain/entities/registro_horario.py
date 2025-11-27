from dataclasses import dataclass
from datetime import datetime, date

@dataclass
class RegistroHorario:
    id: int
    practicante_id: int
    fecha: date
    hora_entrada: datetime | None
    hora_salida: datetime | None
    horas_trabajadas: float | None = None