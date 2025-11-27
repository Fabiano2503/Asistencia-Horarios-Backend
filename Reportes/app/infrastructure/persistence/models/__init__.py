# app/infrastructure/persistence/models/__init__.py
from .base import Base
from .practicante import PracticanteModel
from .registro_horario import RegistroHorarioModel
from .advertencia import AdvertenciaModel
from .permiso import PermisoModel

__all__ = [
    "Base",
    "PracticanteModel",
    "RegistroHorarioModel",
    "AdvertenciaModel",
    "PermisoModel",
]