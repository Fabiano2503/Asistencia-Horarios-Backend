from typing import Dict
from src.domain.ports.horario_repository import HorarioRepository
from src.domain.entities.horario import Horario

class RegistrarHorarioUseCase:
    def __init__(self, repository: HorarioRepository):
        self.repository = repository

    def execute(self, data: Dict) -> Horario:
        horario = Horario(
            practicante=data['practicante'],
            servidor=data['servidor'],
            dia=data['dia'],
            hora_inicio=data['hora_inicio'],
            hora_fin=data['hora_fin']
        )
        return self.repository.save(horario)