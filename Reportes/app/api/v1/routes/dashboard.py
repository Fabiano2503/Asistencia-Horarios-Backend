# app/api/v1/routes/dashboard.py
from fastapi import APIRouter, Depends
from app.application.services.dashboard_service import DashboardService
from app.infrastructure.persistence.database import get_db
from app.infrastructure.persistence.repositories.sql_practicante_repository import SQLPracticanteRepository
from app.infrastructure.persistence.repositories.sql_registro_horario_repository import SQLRegistroHorarioRepository

router = APIRouter()

def get_dashboard_service(db=Depends(get_db)):
    practicante_repo = SQLPracticanteRepository(db)
    registro_repo = SQLRegistroHorarioRepository(db)
    return DashboardService(practicante_repo, registro_repo)

@router.get("/dashboard/summary")
async def resumen_dashboard(service: DashboardService = Depends(get_dashboard_service)):
    return await service.obtener_resumen()