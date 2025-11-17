from dataclasses import dataclass
from typing import Optional

@dataclass
class Servidor:
    id: Optional[int] = None
    nombre: str = ""