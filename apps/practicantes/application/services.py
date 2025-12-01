from typing import List, Optional
from apps.practicantes.domain.practicante import Practicante, EstadoPracticante, Asistencia
from apps.practicantes.domain.repositories import PracticanteRepository, AsistenciaRepository

# Clase de servicio para gestionar la lógica de negocio relacionada con los practicantes
class PracticanteService:

    def __init__(self, practicante_repository: PracticanteRepository):
        self.practicante_repository = practicante_repository

    def get_all_practicantes(self) -> List[Practicante]:
        return self.practicante_repository.get_all()

    def get_practicante_by_id(self, practicante_id: int) -> Optional[Practicante]:
        return self.practicante_repository.get_by_id(practicante_id)

    def create_practicante(self, practicante_data: dict) -> Practicante:
        practicante = Practicante(**practicante_data)
        return self.practicante_repository.create(practicante)

    def update_practicante(self, practicante_id: int, practicante_data: dict) -> Optional[Practicante]:
        practicante = self.get_practicante_by_id(practicante_id)
        if practicante:
            for key, value in practicante_data.items():
                if key == 'estado':
                    setattr(practicante, key, EstadoPracticante(value))
                else:
                    setattr(practicante, key, value)
            return self.practicante_repository.update(practicante)
        return None

    def delete_practicante(self, practicante_id: int) -> None:
        self.practicante_repository.delete(practicante_id)

    def filter_practicantes(self, nombre: Optional[str] = None, correo: Optional[str] = None, estado: Optional[str] = None) -> List[Practicante]:
        return self.practicante_repository.filter(nombre, correo, estado)

    def get_practicante_stats(self) -> dict[str, int]:
        return self.practicante_repository.get_stats()

class AsistenciaService:
    def __init__(self, asistencia_repository):
        self.asistencia_repository = asistencia_repository

    def get_asistencias_by_practicante(self, practicante_id: int):
        return self.asistencia_repository.get_by_practicante(practicante_id)

    def crear_asistencia(self, asistencia_data: dict):
        return self.asistencia_repository.create(asistencia_data)

    def update_asistencia(self, asistencia_id: int, asistencia_data: dict):
        asistencia_data["id"] = asistencia_id
        return self.asistencia_repository.update(asistencia_data)

    def delete_asistencia(self, asistencia_id: int):
        self.asistencia_repository.delete(asistencia_id)

    def get_calendario_semanal(self, practicante_id: int):
        """Retorna el calendario semanal con días y horas trabajadas"""
        return self.asistencia_repository.get_calendario_semanal(practicante_id)

    def get_estadisticas_personales(self, practicante_id: int):
        """Retorna estadísticas personales del practicante"""
        return self.asistencia_repository.get_estadisticas_personales(practicante_id)

class HorarioService:
    def __init__(self, horario_repository):
        self.horario_repository = horario_repository

    def get_horarios_by_practicante(self, practicante_id: int):
        return self.horario_repository.get_by_practicante(practicante_id)

    def crear_horario(self, horario_data: dict):
        return self.horario_repository.create(horario_data)

    def update_horario(self, horario_id: int, horario_data: dict):
        horario_data["id"] = horario_id
        return self.horario_repository.update(horario_data)

    def delete_horario(self, horario_id: int):
        self.horario_repository.delete(horario_id)

class AdvertenciaService:
    def __init__(self, advertencia_repository):
        self.advertencia_repository = advertencia_repository

    def get_advertencias_by_practicante(self, practicante_id: int):
        return self.advertencia_repository.get_by_practicante(practicante_id)

    def crear_advertencia(self, advertencia_data: dict):
        return self.advertencia_repository.create(advertencia_data)

    def update_advertencia(self, advertencia_id: int, advertencia_data: dict):
        advertencia_data["id"] = advertencia_id
        return self.advertencia_repository.update(advertencia_data)

    def delete_advertencia(self, advertencia_id: int):
        self.advertencia_repository.delete(advertencia_id)

    def get_advertencia_stats_by_practicante(self, practicante_id: int):
        return self.advertencia_repository.get_stats_by_practicante(practicante_id)
