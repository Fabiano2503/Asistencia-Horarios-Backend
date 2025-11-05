from typing import List, Optional
from django.db.models import Count, Q
from apps.practicantes.domain.models import Practicante
from apps.practicantes.domain.repositories import PracticanteRepository

# Implementación del repositorio utilizando Django ORM
class DjangoPracticanteRepository(PracticanteRepository):

    def get_all(self) -> List[Practicante]:
        return list(Practicante.objects.all())

    def get_by_id(self, practicante_id: int) -> Optional[Practicante]:
        return Practicante.objects.filter(id=practicante_id).first()

    def create(self, practicante_data: dict) -> Practicante:
        return Practicante.objects.create(**practicante_data)

    def update(self, practicante_id: int, practicante_data: dict) -> Optional[Practicante]:
        practicante = self.get_by_id(practicante_id)
        if practicante:
            for key, value in practicante_data.items():
                setattr(practicante, key, value)
            practicante.save()
        return practicante

    def delete(self, practicante_id: int) -> None:
        practicante = self.get_by_id(practicante_id)
        if practicante:
            practicante.delete()

    def filter(self, nombre: str = None, correo: str = None, estado: str = None) -> List[Practicante]:
        filters = Q()
        if nombre:
            filters &= Q(nombre__icontains=nombre)
        if correo:
            filters &= Q(correo__icontains=correo)
        if estado:
            filters &= Q(estado=estado)
        return list(Practicante.objects.filter(filters))

    def get_stats(self) -> dict:
        total = Practicante.objects.count()
        activos = Practicante.objects.filter(estado=Practicante.Estado.ACTIVO).count()
        en_recuperacion = Practicante.objects.filter(estado=Practicante.Estado.EN_RECUPERACION).count()
        en_riesgo = Practicante.objects.filter(estado=Practicante.Estado.EN_RIESGO).count()
        
        return {
            'total': total,
            'activos': activos,
            'en_recuperacion': en_recuperacion,
            'en_riesgo': en_riesgo
        }
