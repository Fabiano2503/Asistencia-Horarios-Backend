from abc import ABC, abstractmethod
from typing import List, Optional
from apps.practicantes.domain.practicante import Practicante
from apps.practicantes.domain.reforzamiento import PracticanteReforzamiento 

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
    def filter(self, nombre: Optional[str] = None, correo: Optional[str] = None, estado: Optional[str] = None) -> List[Practicante]:
        pass

    @abstractmethod
    def get_stats(self) -> dict[str, int]:
        pass

# Repositorio abstracto para Reforzamiento
class ReforzamientoRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[PracticanteReforzamiento]:
        pass

    @abstractmethod
    def get_by_id(self, reforzamiento_id: int) -> Optional[PracticanteReforzamiento]:
        pass

    @abstractmethod
    def get_by_practicante_id(self, practicante_id: int) -> Optional[PracticanteReforzamiento]:
        pass

    @abstractmethod
    def create(self, reforzamiento: PracticanteReforzamiento) -> PracticanteReforzamiento:
        pass

    @abstractmethod
    def update(self, reforzamiento: PracticanteReforzamiento) -> PracticanteReforzamiento:
        pass

    @abstractmethod
    def delete(self, reforzamiento_id: int) -> None:
        pass

    @abstractmethod
    def filter_by_estado(self, estado: str) -> List[PracticanteReforzamiento]:
        pass

    @abstractmethod
    def get_metricas(self) -> dict:
        pass