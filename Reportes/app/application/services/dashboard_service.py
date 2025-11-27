from datetime import datetime, timedelta
from app.ports.repositories.practicante_repository import IPracticanteRepository
from app.ports.repositories.registro_horario_repository import IRegistroHorarioRepository

class DashboardService:
    def __init__(self, practicante_repo: IPracticanteRepository, registro_repo: IRegistroHorarioRepository):
        self.practicante_repo = practicante_repo
        self.registro_repo = registro_repo

    async def obtener_resumen(self):
        practicantes = await self.practicante_repo.listar_con_advertencias()
        hoy = datetime.utcnow().date()
        inicio_semana = hoy - timedelta(days=hoy.weekday())
        fin_semana = inicio_semana + timedelta(days=6)

        horas_totales = await self.registro_repo.total_horas_semana(inicio_semana, fin_semana)
        horas_totales = round(horas_totales, 1)

        # Meta semanal: 40 horas por practicante (lunes a viernes)
        meta_semanal = len(practicantes) * 40.0 if practicantes else 0.0
        horas_faltantes = max(0.0, round(meta_semanal - horas_totales, 1))
        porcentaje = round((horas_totales / meta_semanal) * 100, 1) if meta_semanal > 0 else 0.0

        return {
            "horasTotalesSemana": horas_totales,
            "horasFaltantesMetaGeneral": horas_faltantes,
            "cumplimientoMetaGeneralPorcentaje": porcentaje
        }