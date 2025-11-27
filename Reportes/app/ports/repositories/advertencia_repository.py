# app/ports/repositories/advertencia_repository.py
from abc import ABC, abstractmethod

class IAdvertenciaRepository(ABC):
    @abstractmethod
    async def contar_por_practicante(self, practicante_id: int) -> int:
        pass