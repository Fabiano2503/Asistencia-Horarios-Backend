# app/infrastructure/persistence/models/advertencia.py
from sqlalchemy import Column, Integer, Date, String, ForeignKey
from .base import Base

class AdvertenciaModel(Base):
    __tablename__ = "advertencias"

    id = Column(Integer, primary_key=True)
    practicante_id = Column(Integer, ForeignKey("practicantes.id"), nullable=False)
    fecha = Column(Date, nullable=False)
    motivo = Column(String(200), nullable=False)