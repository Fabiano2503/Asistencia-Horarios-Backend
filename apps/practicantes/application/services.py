from typing import List, Optional
from apps.practicantes.domain.practicante import Practicante, EstadoPracticante
from apps.practicantes.domain.repositories import PracticanteRepository

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
