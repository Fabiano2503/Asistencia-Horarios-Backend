from src.domain.ports.horario_repository import HorarioRepository
from src.domain.entities.horario import Horario
from horario_app.models import Horario as HorarioModel, Practicante
from typing import List, Optional

class HorarioRepositoryImpl(HorarioRepository):
    def _to_entity(self, model: HorarioModel) -> Horario:
        return Horario(
            id=model.id,
            practicante_id=model.practicante_id,
            servidor_id=model.practicante.servidor_id,
            dia=model.dia,
            hora_inicio=model.hora_inicio.strftime("%H:%M"),
            hora_fin=model.hora_fin.strftime("%H:%M"),
            estado=model.estado
        )

    def save(self, horario: Horario) -> Horario:
        obj = HorarioModel.objects.create(
            practicante_id=horario.practicante_id,
            dia=horario.dia,
            hora_inicio=horario.hora_inicio,
            hora_fin=horario.hora_fin
        )
        horario.id = obj.id
        return horario

    def find_all(self, servidor_id: Optional[int] = None) -> List[Horario]:
        queryset = HorarioModel.objects.select_related('practicante__servidor')
        if servidor_id:
            queryset = queryset.filter(practicante__servidor_id=servidor_id)
        return [self._to_entity(h) for h in queryset]

    def find_pendientes(self) -> List[Horario]:
        return [self._to_entity(h) for h in HorarioModel.objects.filter(estado='pendiente')]

    def find_by_practicante(self, practicante_id: int) -> List[Horario]:
        return [self._to_entity(h) for h in HorarioModel.objects.filter(practicante_id=practicante_id)]