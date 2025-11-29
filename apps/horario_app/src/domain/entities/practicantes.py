from dataclasses import dataclass
from typing import Optional

@dataclass
class Practicante:
    id: Optional[int] = None
    nombre: str = ""