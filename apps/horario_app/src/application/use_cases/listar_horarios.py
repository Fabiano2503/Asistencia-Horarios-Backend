from src.domain.ports.horario_repository import HorarioRepository

class ListarHorariosUseCase:
    def __init__(self, repository: HorarioRepository):
        self.repository = repository

    def execute(self, servidor_id=None):
        return self.repository.find_all(servidor_id)