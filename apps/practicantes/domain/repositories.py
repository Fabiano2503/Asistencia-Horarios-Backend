from abc import ABC, abstractmethod
from typing import List, Optional
from apps.practicantes.domain.practicante import Practicante

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

class AsistenciaRepository(ABC):
    @abstractmethod
    def get_by_practicante(self, practicante_id: int) -> list:
        pass
    @abstractmethod
    def create(self, asistencia) -> object:
        pass
    @abstractmethod
    def update(self, asistencia) -> object:
        pass
    @abstractmethod
    def delete(self, asistencia_id: int) -> None:
        pass

class HorarioRepository(ABC):
    @abstractmethod
    def get_by_practicante(self, practicante_id: int) -> list:
        pass
    @abstractmethod
    def create(self, horario) -> object:
        pass
    @abstractmethod
    def update(self, horario) -> object:
        pass
    @abstractmethod
    def delete(self, horario_id: int) -> None:
        pass

class AdvertenciaRepository(ABC):
    @abstractmethod
    def get_by_practicante(self, practicante_id: int) -> list:
        pass
    @abstractmethod
    def create(self, advertencia) -> object:
        pass
    @abstractmethod
    def update(self, advertencia) -> object:
        pass
    @abstractmethod
    def delete(self, advertencia_id: int) -> None:
        pass
    @abstractmethod
    def get_stats_by_practicante(self, practicante_id: int) -> dict:
        pass
