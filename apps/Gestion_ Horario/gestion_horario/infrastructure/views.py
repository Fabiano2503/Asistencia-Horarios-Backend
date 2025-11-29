from fastapi import HTTPException, APIRouter
from gestion_horario.application.services import DashboardService, HorarioService, RecuperacionService
from gestion_horario.infrastructure.serializers import *
from gestion_horario.infrastructure.django_orm_repository import PracticanteRepository

# Repositorios
practicante_repo = PracticanteRepository()
dashboard_service = DashboardService(practicante_repo)
horario_service = HorarioService(practicante_repo)
recuperacion_service = RecuperacionService(practicante_repo)

# 1. Dashboard Summary
async def get_dashboard_summary():
    return await dashboard_service.get_summary()

# 2. Vista Semanal
async def get_vista_semanal():
    return await horario_service.get_vista_semanal()

# 3. Listar practicantes
async def listar_practicantes():
    practicantes = await practicante_repo.list_all_with_horario()
    return [practicante_to_dict(p) for p in practicantes]

# 4. Horario de un practicante
async def get_horario_practicante(practicante_id: int):
    practicante = await practicante_repo.get_with_horario(practicante_id)
    if not practicante:
        raise HTTPException(404, "Practicante no encontrado")
    return horario_to_dict(practicante.horarios)

# 5. Actualizar horario
async def actualizar_horario_practicante(practicante_id: int, data: dict):
    await horario_service.actualizar_horario(practicante_id, data)
    return {"message": "Horario actualizado"}

# 6. Pendientes de aprobación
async def get_pendientes_aprobacion():
    return await recuperacion_service.get_pendientes()

# 7. Detalle recuperación
async def get_detalle_recuperacion(id: int):
    rec = await recuperacion_service.get_by_id(id)
    if not rec:
        raise HTTPException(404, "No encontrado")
    return recuperacion_to_dict(rec)

# 8. Aprobar
async def aprobar_recuperacion(id: int):
    await recuperacion_service.aprobar(id)
    return {"message": "Recuperación aprobada"}

# 9. Rechazar
async def rechazar_recuperacion(id: int, motivo: str):
    await recuperacion_service.rechazar(id, motivo)
    return {"message": "Recuperación rechazada"}

# 10. Registrar horario con evidencia
async def registrar_horario_con_evidencia(practicante_id: int, foto: bytes, bloques: list):
    await horario_service.registrar_con_evidencia(practicante_id, foto, bloques)
    return {"message": "Horario enviado para aprobación"}

# 11. Servidores
async def get_servidores():
    return ["Rpsoft", "SENATI", "Innovación", "MiniBootcamp", "Laboratorios", "Recuperación"]