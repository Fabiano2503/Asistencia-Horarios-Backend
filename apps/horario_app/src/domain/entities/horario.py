from dataclasses import dataclass
from typing import Optional

@dataclass
class Horario:
    id: Optional[int] = None
    practicante: Optional[object] = None  # ← Acepta modelo Django
    servidor: Optional[object] = None     # ← Acepta modelo Django
    dia: str = ""
    hora_inicio: str = ""
    hora_fin: str = ""
    estado: str = "pendiente"