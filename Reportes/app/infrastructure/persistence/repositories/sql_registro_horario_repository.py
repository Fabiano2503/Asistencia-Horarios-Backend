from datetime import date, datetime, time
from sqlalchemy import select, func
from app.domain.entities.registro_horario import RegistroHorario
from app.ports.repositories.registro_horario_repository import IRegistroHorarioRepository
from app.infrastructure.persistence.models.registro_horario import RegistroHorarioModel

class SQLRegistroHorarioRepository(IRegistroHorarioRepository):
    def __init__(self, session):
        self.session = session

    async def total_horas_semana(self, inicio: date, fin: date) -> float:
        # Calcula horas entre entrada y salida (en horas decimales)
        query = select(
            func.sum(
                func.extract('epoch', 
                    func.coalesce(RegistroHorarioModel.hora_salida, datetime.utcnow()) - 
                    RegistroHorarioModel.hora_entrada
                ) / 3600
            )
        ).where(
            RegistroHorarioModel.fecha.between(inicio, fin),
            RegistroHorarioModel.hora_entrada.is_not(None)
        )
        result = await self.session.execute(query)
        total = result.scalar() or 0.0
        return float(total)

    async def obtener_por_practicante(self, practicante_id: int):
        query = select(RegistroHorarioModel).where(RegistroHorarioModel.practicante_id == practicante_id)
        result = await self.session.execute(query)
        rows = result.scalars().all()
        return [RegistroHorario(
            id=r.id,
            practicante_id=r.practicante_id,
            fecha=r.fecha,
            hora_entrada=r.hora_entrada,
            hora_salida=r.hora_salida
        ) for r in rows]