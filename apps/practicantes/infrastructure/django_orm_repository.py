from typing import List, Optional
from django.db.models import Q
from apps.practicantes.domain.practicante import Practicante, EstadoPracticante
from apps.practicantes.domain.repositories import PracticanteRepository,  ReforzamientoRepository
from apps.practicantes.domain.reforzamiento import PracticanteReforzamiento as ReforzamientoDomain, EstadoReforzamiento  
from apps.practicantes.infrastructure.models import Practicante as PracticanteModel
from .models import Practicante as PracticanteModel, PracticanteReforzamiento as ReforzamientoModel  

# Implementación del repositorio utilizando Django ORM
class DjangoPracticanteRepository(PracticanteRepository):

    def _to_domain(self, model: PracticanteModel) -> Practicante:
        return Practicante(
            id=model.id,
            id_discord=model.id_discord,
            nombre=model.nombre,
            apellido=model.apellido,
            correo=model.correo,
            semestre=model.semestre,
            estado=EstadoPracticante(model.estado)
        )

    # Convierte entidad a modelo Django
    def _to_model(self, entity: Practicante, model: PracticanteModel = None) -> PracticanteModel:
        if model is None:
            model = PracticanteModel()
        model.id_discord = entity.id_discord
        model.nombre = entity.nombre
        model.apellido = entity.apellido
        model.correo = entity.correo
        model.semestre = entity.semestre
        model.estado = entity.estado.value if isinstance(entity.estado, EstadoPracticante) else entity.estado
        return model

    # Implementación de los métodos del repositorio abstracto
    def get_all(self) -> List[Practicante]:
        return [self._to_domain(m) for m in PracticanteModel.objects.all()]

    def get_by_id(self, id: int) -> Optional[Practicante]:
        model = PracticanteModel.objects.filter(id=id).first()
        return self._to_domain(model) if model else None

    def create(self, practicante: Practicante) -> Practicante:
        model = self._to_model(practicante)
        model.save()
        return self._to_domain(model)

    def update(self, practicante: Practicante) -> Practicante:
        model = PracticanteModel.objects.filter(id=practicante.id).first()
        if model is None:
            raise ValueError(f"Practicante con id {practicante.id} no encontrado.")
        
        # Actualizar los campos del modelo existente
        model = self._to_model(practicante, model)
        model.save()
        
        return self._to_domain(model)

    def delete(self, id: int) -> None:
        PracticanteModel.objects.filter(id=id).delete()

    def filter(self, nombre: str = None, correo: str = None, estado: str = None) -> List[Practicante]:
        q = Q()
        if nombre:
            q &= Q(nombre__icontains=nombre)
        if correo:
            q &= Q(correo__icontains=correo)
        if estado:
            q &= Q(estado=estado)
        return [self._to_domain(m) for m in PracticanteModel.objects.filter(q)]

    def get_stats(self) -> dict:
        total = PracticanteModel.objects.count()
        activos = PracticanteModel.objects.filter(estado=EstadoPracticante.ACTIVO.value).count()
        en_recuperacion = PracticanteModel.objects.filter(estado=EstadoPracticante.EN_RECUPERACION.value).count()
        en_riesgo = PracticanteModel.objects.filter(estado=EstadoPracticante.EN_RIESGO.value).count()
        return {
            "total": total,
            "activos": activos,
            "en_recuperacion": en_recuperacion,
            "en_riesgo": en_riesgo
        }

# Implementación del repositorio de Reforzamiento usando Django ORM
class DjangoReforzamientoRepository(ReforzamientoRepository):

    def _to_domain(self, model: ReforzamientoModel) -> ReforzamientoDomain:
        return ReforzamientoDomain(
            id=model.id,
            practicante_id=model.practicante_id,
            nombre_completo=model.nombre_completo,
            area=model.area,
            motivo=model.motivo,
            fecha_ingreso=model.fecha_ingreso,
            estado=EstadoReforzamiento(model.estado)
        )

    def _to_model(self, domain: ReforzamientoDomain) -> ReforzamientoModel:
        if domain.id:
            model = ReforzamientoModel.objects.get(id=domain.id)
            model.practicante_id = domain.practicante_id
            model.nombre_completo = domain.nombre_completo
            model.area = domain.area
            model.motivo = domain.motivo
            model.fecha_ingreso = domain.fecha_ingreso
            model.estado = domain.estado.value
        else:
            model = ReforzamientoModel(
                practicante_id=domain.practicante_id,
                nombre_completo=domain.nombre_completo,
                area=domain.area,
                motivo=domain.motivo,
                fecha_ingreso=domain.fecha_ingreso,
                estado=domain.estado.value
            )
        return model

    def get_all(self) -> List[ReforzamientoDomain]:
        models = ReforzamientoModel.objects.all()
        return [self._to_domain(model) for model in models]

    def get_by_id(self, reforzamiento_id: int) -> Optional[ReforzamientoDomain]:
        try:
            model = ReforzamientoModel.objects.get(id=reforzamiento_id)
            return self._to_domain(model)
        except ReforzamientoModel.DoesNotExist:
            return None

    def get_by_practicante_id(self, practicante_id: int) -> Optional[ReforzamientoDomain]:
        try:
            model = ReforzamientoModel.objects.filter(practicante_id=practicante_id).first()
            return self._to_domain(model) if model else None
        except ReforzamientoModel.DoesNotExist:
            return None

    def create(self, reforzamiento: ReforzamientoDomain) -> ReforzamientoDomain:
        model = self._to_model(reforzamiento)
        model.save()
        return self._to_domain(model)

    def update(self, reforzamiento: ReforzamientoDomain) -> ReforzamientoDomain:
        model = self._to_model(reforzamiento)
        model.save()
        return self._to_domain(model)

    def delete(self, reforzamiento_id: int) -> None:
        ReforzamientoModel.objects.filter(id=reforzamiento_id).delete()

    def filter_by_estado(self, estado: str) -> List[ReforzamientoDomain]:
        models = ReforzamientoModel.objects.filter(estado=estado)
        return [self._to_domain(model) for model in models]

    def get_metricas(self) -> dict:
        en_reforzamiento = ReforzamientoModel.objects.filter(
            estado=ReforzamientoModel.Estado.EN_REFORZAMIENTO
        ).count()
        
        completados = ReforzamientoModel.objects.filter(
            estado=ReforzamientoModel.Estado.COMPLETADO
        ).count()
        
        reintegrados = ReforzamientoModel.objects.filter(
            estado=ReforzamientoModel.Estado.REINTEGRADO
        ).count()
        
        return {
            'en_reforzamiento': en_reforzamiento,
            'completados': completados,
            'reintegrados': reintegrados
        }