from abc import ABC, abstractmethod
from typing import List, Optional
from .models import Practicante

# Repositorio abstracto para el modelo Practicante
class PracticanteRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[Practicante]:
        pass

    @abstractmethod
    def get_by_id(self, practicante_id: int) -> Optional[Practicante]:
        pass

    @abstractmethod
    def create(self, practicante: Practicante) -> Practicante:
        pass

    @abstractmethod
    def update(self, practicante: Practicante) -> Practicante:
        pass

    @abstractmethod
    def delete(self, practicante_id: int) -> None:
        pass

    @abstractmethod
    def filter(self, nombre: str = None, correo: str = None, estado: str = None) -> List[Practicante]:
        pass

    @abstractmethod
    def get_stats(self) -> dict:
        pass
