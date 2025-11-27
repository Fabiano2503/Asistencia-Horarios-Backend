from dataclasses import dataclass
from enum import Enum
from typing import Optional

# Definición de los posibles estados de un practicante
class EstadoPracticante(Enum):
    ACTIVO = "activo"
    EN_RECUPERACION = "en_recuperacion"
    EN_RIESGO = "en_riesgo"


# Entidad de dominio que representa a un practicante
@dataclass
class Practicante:
    id_discord: int
    nombre: str
    apellido: str
    correo: str
    semestre: int
    estado: EstadoPracticante = EstadoPracticante.ACTIVO
    id: Optional[int] = None

    # Validaciones al crear una instancia
    def __post_init__(self):
        if self.semestre < 1 or self.semestre > 6:
            raise ValueError("El semestre debe estar entre 1 y 6.")

    # Método para obtener el nombre completo
    @property
    def nombre_completo(self) -> str:
        return f"{self.nombre} {self.apellido}"

    # Método para cambiar el estado del practicante
    def cambiar_estado(self, nuevo_estado: EstadoPracticante):
        self.estado = nuevo_estado

    # Métodos específicos para cambiar el estado
    def marcar_en_riesgo(self):
        self.cambiar_estado(EstadoPracticante.EN_RIESGO)

    def marcar_en_recuperacion(self):
        self.cambiar_estado(EstadoPracticante.EN_RECUPERACION)

    def activar(self):
        self.cambiar_estado(EstadoPracticante.ACTIVO)

    def __str__(self):
        return f"[{self.id_discord}] {self.nombre_completo} - {self.estado.value}"

# Entidad de dominio que representa una asistencia
@dataclass
class Asistencia:
    id: Optional[int]
    practicante_id: int
    fecha: str  # Formato 'YYYY-MM-DD'
    hora_entrada: str  # Formato 'HH:MM:SS'
    hora_salida: Optional[str] = None

# Entidad de dominio que representa un horario
@dataclass
class Horario:
    id: Optional[int]
    practicante_id: int
    dia_semana: str  # Ejemplo: 'lunes', 'martes', ...
    hora_inicio: str  # Formato 'HH:MM:SS'
    hora_fin: str  # Formato 'HH:MM:SS'

# Entidad de dominio que representa una advertencia
@dataclass
class Advertencia:
    id: Optional[int]
    practicante_id: int
    tipo: str  # 'retraso', 'falta', 'inasistencia', 'otro'
    gravedad: str  # 'leve', 'moderada', 'grave'
    descripcion: str
    fecha: str  # Formato 'YYYY-MM-DD'
    resuelta: bool = False
    fecha_resolucion: Optional[str] = None
