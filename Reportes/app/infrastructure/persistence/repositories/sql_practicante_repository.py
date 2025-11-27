from typing import List
from sqlalchemy import select, func
from app.domain.entities.practicante import Practicante
from app.ports.repositories.practicante_repository import IPracticanteRepository
from app.infrastructure.persistence.models.practicante import PracticanteModel
from app.infrastructure.persistence.models.advertencia import AdvertenciaModel

class SQLPracticanteRepository(IPracticanteRepository):
    def __init__(self, session):
        self.session = session

    async def listar_con_advertencias(self) -> List[Practicante]:
        query = (
            select(
                PracticanteModel.id,
                PracticanteModel.nombre,
                PracticanteModel.area,
                func.coalesce(func.count(AdvertenciaModel.id), 0).label("advertencias_cnt")
            )
            .outerjoin(AdvertenciaModel, PracticanteModel.id == AdvertenciaModel.practicante_id)
            .group_by(PracticanteModel.id)
        )
        result = await self.session.execute(query)
        rows = result.all()

        return [
            Practicante(
                id=row.id,
                nombre=row.nombre,
                area=row.area,
                meta_horas_mensual=240.0
            ) for row in rows
        ]

    # AÑADIMOS ESTE MÉTODO QUE FALTABA (obligatorio por la interfaz)
    async def obtener_por_id(self, practicante_id: int) -> Practicante | None:
        query = select(PracticanteModel).where(PracticanteModel.id == practicante_id)
        result = await self.session.execute(query)
        row = result.scalar_one_or_none()
        if not row:
            return None
        return Practicante(
            id=row.id,
            nombre=row.nombre,
            area=row.area,
            meta_horas_mensual=row.meta_horas_mensual or 240.0
        )