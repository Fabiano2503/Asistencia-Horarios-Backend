# app/infrastructure/persistence/models/registro_horario.py
from sqlalchemy import Column, Integer, Date, DateTime, ForeignKey
from .base import Base

class RegistroHorarioModel(Base):
    __tablename__ = "registros_horarios"

    id = Column(Integer, primary_key=True)
    practicante_id = Column(Integer, ForeignKey("practicantes.id"), nullable=False)
    fecha = Column(Date, nullable=False)
    hora_entrada = Column(DateTime)
    hora_salida = Column(DateTime)