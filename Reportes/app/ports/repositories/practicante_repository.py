from abc import ABC, abstractmethod
from typing import List
from app.domain.entities.practicante import Practicante

class IPracticanteRepository(ABC):
    @abstractmethod
    async def listar_con_advertencias(self) -> List[Practicante]:
        pass

    @abstractmethod
    async def obtener_por_id(self, practicante_id: int) -> Practicante | None:
        pass