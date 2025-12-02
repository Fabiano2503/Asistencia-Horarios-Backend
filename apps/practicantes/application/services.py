from typing import List, Optional
from apps.practicantes.domain.practicante import Practicante, EstadoPracticante
from apps.practicantes.domain.repositories import PracticanteRepository

# Clase de servicio para gestionar la lógica de negocio relacionada con los practicantes
class PracticanteService:

    def __init__(self, practicante_repository: PracticanteRepository):
        self.practicante_repository = practicante_repository

    # ... (Tus métodos CRUD y filter, get_stats aquí) ...
    
    # ----------------------------------------------------
    # MÉTODOS DE REPORTES (AGREGADOS PARA CORREGIR EL BUG)
    # ----------------------------------------------------

    def get_advertencias_historico(self):
        """Devuelve el histórico de advertencias de los practicantes."""
        # TODO: Implementar lógica llamando al repositorio/otros servicios
        return []

    def get_advertencias_mes_actual(self):
        """Devuelve las advertencias del mes actual."""
        # TODO: Implementar lógica llamando al repositorio/otros servicios
        return []

    def get_permisos_por_practicante(self):
        """Devuelve los permisos agrupados por practicante."""
        # TODO: Implementar lógica llamando al repositorio/otros servicios
        return []

    def get_permisos_semana_actual(self):
        """Devuelve los permisos registrados en la semana actual."""
        # TODO: Implementar lógica llamando al repositorio/otros servicios
        return []

    # ----------------------------------------------------
    # (Resto de tu código CRUD original, por ejemplo):
    
    def get_all_practicantes(self) -> List[Practicante]:
        return self.practicante_repository.get_all()
    
    # ... (Resto de tus métodos aquí) ...
    def filter_practicantes(self, nombre: Optional[str] = None, correo: Optional[str] = None, estado: Optional[str] = None) -> List[Practicante]:
        return self.practicante_repository.filter(nombre, correo, estado)

    def get_practicante_stats(self) -> dict[str, int]:
        return self.practicante_repository.get_stats()
