# app/infrastructure/urls.py
from fastapi import APIRouter
from .views import (
    get_dashboard_summary, get_vista_semanal, listar_practicantes, get_horario_practicante,
    actualizar_horario_practicante, get_pendientes_aprobacion, get_detalle_recuperacion,
    aprobar_recuperacion, rechazar_recuperacion, registrar_horario_con_evidencia, get_servidores
)

router = APIRouter()

# DASHBOARD
router.get("/api/v1/dashboard/summary")(get_dashboard_summary)

# VISTA SEMANAL
router.get("/api/v1/horarios/semanales")(get_vista_semanal)

# PRACTICANTES
router.get("/api/v1/practicantes")(listar_practicantes)
router.get("/api/v1/practicantes/{practicante_id}/horario")(get_horario_practicante)
router.put("/api/v1/practicantes/{practicante_id}/horario")(actualizar_horario_practicante)

# RECUPERACIONES (PENDIENTES)
router.get("/api/v1/recuperaciones/pendientes")(get_pendientes_aprobacion)
router.get("/api/v1/recuperaciones/{id}")(get_detalle_recuperacion)
router.post("/api/v1/recuperaciones/{id}/aprobar")(aprobar_recuperacion)
router.post("/api/v1/recuperaciones/{id}/rechazar")(rechazar_recuperacion)

# REGISTRAR HORARIO (BOTÓN AZUL)
router.post("/api/v […]")



# SERVIDORES
router.get("/api/v1/servidores")(get_servidores)