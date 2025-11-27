from typing import List, Optional
from django.db.models import Q
from datetime import datetime, timedelta
from apps.practicantes.domain.practicante import Practicante, EstadoPracticante, Asistencia as AsistenciaDomain, Horario as HorarioDomain, Advertencia as AdvertenciaDomain
from apps.practicantes.domain.repositories import PracticanteRepository, AsistenciaRepository, HorarioRepository, AdvertenciaRepository
from apps.practicantes.infrastructure.models import Practicante as PracticanteModel, Asistencia as AsistenciaModel, Horario as HorarioModel, Advertencia as AdvertenciaModel

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

class DjangoAsistenciaRepository(AsistenciaRepository):
    def get_by_practicante(self, practicante_id: int):
        return [self._to_domain(a) for a in AsistenciaModel.objects.filter(practicante_id=practicante_id)]
    def create(self, asistencia_data: dict):
        a = AsistenciaModel.objects.create(**asistencia_data)
        return self._to_domain(a)
    def update(self, asistencia_data: dict):
        a = AsistenciaModel.objects.filter(id=asistencia_data["id"]).first()
        if not a:
            raise ValueError("No se encontró la asistencia")
        for k, v in asistencia_data.items():
            if hasattr(a, k):
                setattr(a, k, v)
        a.save()
        return self._to_domain(a)
    def delete(self, asistencia_id: int):
        AsistenciaModel.objects.filter(id=asistencia_id).delete()

    def get_calendario_semanal(self, practicante_id: int):
        """Retorna el calendario semanal con días y horas trabajadas"""
        today = datetime.now().date()
        # Calcular el lunes de la semana actual
        monday = today - timedelta(days=today.weekday())
        sunday = monday + timedelta(days=6)

        calendario = []
        for i in range(7):
            current_date = monday + timedelta(days=i)
            asistencia = AsistenciaModel.objects.filter(
                practicante_id=practicante_id,
                fecha=current_date
            ).first()

            horas_trabajadas = 0.0
            trabajó = False

            if asistencia and asistencia.hora_entrada and asistencia.hora_salida:
                trabajó = True
                entrada = datetime.combine(current_date, asistencia.hora_entrada)
                salida = datetime.combine(current_date, asistencia.hora_salida)
                horas_trabajadas = (salida - entrada).total_seconds() / 3600

            calendario.append({
                "fecha": str(current_date),
                "dia_semana": ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"][i],
                "trabajó": trabajó,
                "horas_trabajadas": round(horas_trabajadas, 2)
            })

        return calendario

    def get_estadisticas_personales(self, practicante_id: int):
        """Retorna estadísticas personales del practicante para la semana actual"""
        today = datetime.now().date()
        monday = today - timedelta(days=today.weekday())
        sunday = monday + timedelta(days=6)

        asistencias_semana = AsistenciaModel.objects.filter(
            practicante_id=practicante_id,
            fecha__range=[monday, sunday]
        )

        total_dias_trabajados = 0
        total_horas_semana = 0.0
        dias_con_asistencia_completa = 0

        for asistencia in asistencias_semana:
            if asistencia.hora_entrada and asistencia.hora_salida:
                total_dias_trabajados += 1
                entrada = datetime.combine(asistencia.fecha, asistencia.hora_entrada)
                salida = datetime.combine(asistencia.fecha, asistencia.hora_salida)
                horas_dia = (salida - entrada).total_seconds() / 3600
                total_horas_semana += horas_dia

                # Considerar asistencia completa si trabajó al menos 4 horas
                if horas_dia >= 4.0:
                    dias_con_asistencia_completa += 1

        promedio_horas_diario = total_horas_semana / total_dias_trabajados if total_dias_trabajados > 0 else 0

        return {
            "semana_actual": {
                "inicio": str(monday),
                "fin": str(sunday)
            },
            "dias_trabajados": total_dias_trabajados,
            "dias_con_asistencia_completa": dias_con_asistencia_completa,
            "total_horas_semana": round(total_horas_semana, 2),
            "promedio_horas_diario": round(promedio_horas_diario, 2),
            "dias_semana_total": 7
        }

    def _to_domain(self, model):
        return AsistenciaDomain(
            id=model.id,
            practicante_id=model.practicante_id,
            fecha=str(model.fecha),
            hora_entrada=str(model.hora_entrada),
            hora_salida=str(model.hora_salida) if model.hora_salida else None
        )

class DjangoHorarioRepository(HorarioRepository):
    def get_by_practicante(self, practicante_id: int):
        return [self._to_domain(h) for h in HorarioModel.objects.filter(practicante_id=practicante_id)]
    def create(self, horario_data: dict):
        h = HorarioModel.objects.create(**horario_data)
        return self._to_domain(h)
    def update(self, horario_data: dict):
        h = HorarioModel.objects.filter(id=horario_data["id"]).first()
        if not h:
            raise ValueError("No se encontró el horario")
        for k, v in horario_data.items():
            if hasattr(h, k):
                setattr(h, k, v)
        h.save()
        return self._to_domain(h)
    def delete(self, horario_id: int):
        HorarioModel.objects.filter(id=horario_id).delete()
    def _to_domain(self, model):
        return HorarioDomain(
            id=model.id,
            practicante_id=model.practicante_id,
            dia_semana=model.dia_semana,
            hora_inicio=str(model.hora_inicio),
            hora_fin=str(model.hora_fin),
        )

class DjangoAdvertenciaRepository(AdvertenciaRepository):
    def get_by_practicante(self, practicante_id: int):
        return [self._to_domain(a) for a in AdvertenciaModel.objects.filter(practicante_id=practicante_id)]
    def create(self, advertencia_data: dict):
        a = AdvertenciaModel.objects.create(**advertencia_data)
        return self._to_domain(a)
    def update(self, advertencia_data: dict):
        a = AdvertenciaModel.objects.filter(id=advertencia_data["id"]).first()
        if not a:
            raise ValueError("No se encontró la advertencia")
        for k, v in advertencia_data.items():
            if hasattr(a, k):
                setattr(a, k, v)
        a.save()
        return self._to_domain(a)
    def delete(self, advertencia_id: int):
        AdvertenciaModel.objects.filter(id=advertencia_id).delete()
    def get_stats_by_practicante(self, practicante_id: int):
        total = AdvertenciaModel.objects.filter(practicante_id=practicante_id).count()
        leves = AdvertenciaModel.objects.filter(practicante_id=practicante_id, gravedad='leve').count()
        moderadas = AdvertenciaModel.objects.filter(practicante_id=practicante_id, gravedad='moderada').count()
        graves = AdvertenciaModel.objects.filter(practicante_id=practicante_id, gravedad='grave').count()
        resueltas = AdvertenciaModel.objects.filter(practicante_id=practicante_id, resuelta=True).count()
        pendientes = total - resueltas
        return {
            "total": total,
            "leves": leves,
            "moderadas": moderadas,
            "graves": graves,
            "resueltas": resueltas,
            "pendientes": pendientes
        }
    def _to_domain(self, model):
        return AdvertenciaDomain(
            id=model.id,
            practicante_id=model.practicante_id,
            tipo=model.tipo,
            gravedad=model.gravedad,
            descripcion=model.descripcion,
            fecha=str(model.fecha),
            resuelta=model.resuelta,
            fecha_resolucion=str(model.fecha_resolucion) if model.fecha_resolucion else None
        )
