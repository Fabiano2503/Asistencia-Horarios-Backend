from dataclasses import dataclass

@dataclass
class Practicante:
    id: int
    nombre: str
    area: str
    meta_horas_mensual: float = 240.0