# app/ports/repositories/__init__.py
from .practicante_repository import IPracticanteRepository
from .registro_horario_repository import IRegistroHorarioRepository

__all__ = [
    "IPracticanteRepository",
    "IRegistroHorarioRepository",
    "IAdvertenciaRepository",
]