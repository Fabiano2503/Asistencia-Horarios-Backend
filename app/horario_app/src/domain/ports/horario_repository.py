from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.horario import Horario

class HorarioRepository(ABC):
    @abstractmethod
    def save(self, horario: Horario) -> Horario:
        pass

    @abstractmethod
    def find_all(self, servidor_id: Optional[int] = None) -> List[Horario]:
        pass

    @abstractmethod
    def find_pendientes(self) -> List[Horario]:
        pass

    @abstractmethod
    def find_by_practicante(self, practicante_id: int) -> List[Horario]:
        pass