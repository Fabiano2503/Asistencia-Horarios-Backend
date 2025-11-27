from abc import ABC, abstractmethod
from datetime import date
from typing import List
from app.domain.entities.registro_horario import RegistroHorario

class IRegistroHorarioRepository(ABC):
    @abstractmethod
    async def total_horas_semana(self, inicio: date, fin: date) -> float:
        """Devuelve total de horas trabajadas en un rango de fechas"""
        pass

    @abstractmethod
    async def obtener_por_practicante(self, practicante_id: int) -> List[RegistroHorario]:
        pass