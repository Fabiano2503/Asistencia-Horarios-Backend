from sqlalchemy import Column, Integer, String, Float
from .base import Base

class PracticanteModel(Base):
    __tablename__ = "practicantes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    area = Column(String, nullable=False)
    meta_horas_mensual = Column(Float, default=240.0)