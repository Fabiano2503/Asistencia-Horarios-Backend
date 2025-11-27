
from sqlalchemy import Column, Integer, Date, String, Boolean, ForeignKey
from .base import Base

class PermisoModel(Base):
    __tablename__ = "permisos"

    id = Column(Integer, primary_key=True)
    practicante_id = Column(Integer, ForeignKey("practicantes.id"), nullable=False)
    fecha_inicio = Column(Date, nullable=False)
    fecha_fin = Column(Date, nullable=False)
    tipo = Column(String(50), nullable=False)
    aprobado = Column(Boolean, default=True)