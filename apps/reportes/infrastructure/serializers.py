# app/infrastructure/serializers.py

from datetime import date, datetime
from typing import Optional

class PracticanteBase(BaseModel):
    id: int
    nombre: str
    apellido: str
    correo: str
    semestre: int

class AdvertenciaMesActual(BaseModel):
    practicante: PracticanteBase
    cantidad_advertencias: int

class HistorialAdvertencia(BaseModel):
    practicante: PracticanteBase
    fecha: date
    motivo: str
    tipo: str  # unjustified-absence, unanswered-call, etc.

class DetalleCumplimientoHoras(BaseModel):
    practicante: PracticanteBase
    horas_semanales: float = 0.0
    proyeccion_mensual: float = 0.0
    porcentaje_meta: float = 0.0
    estado: str  # "critical", "warning", "ok"

class ResumenGlobalHoras(BaseModel):
    total_horas_trabajadas: float
    meta_semanal_total: int = 240
    porcentaje_cumplimiento: float
    practicantes_cumpliendo: int
    practicantes_criticos: int
    total_practicantes: int

class PermisoSemana(BaseModel):
    id: int
    practicante: PracticanteBase
    fecha_solicitud: date
    motivo: str
    estado: str  # Aprobado / Pendiente / Rechazado

class ResumenPermisosPracticante(BaseModel):
    practicante: PracticanteBase
    aprobados: int
    total_solicitados: int

class DashboardSummary(BaseModel):
    total_horas: float
    meta_semanal: int = 240
    cumplimiento_porcentaje: float
    horas_faltantes: float
