# app/main.py
from fastapi import FastAPI
from app.infrastructure.persistence.database import engine
from app.infrastructure.persistence.models import Base  # importa TODOS los modelos
import asyncio

app = FastAPI(
    title="Control de Horas - Practicantes",
    version="1.0.0",
    description="Backend hexagonal 100% funcional"
)

# type: ignore

# CREA LAS TABLAS AUTOMÁTICAMENTE al iniciar (solo desarrollo)
@app.on_event("startup")
async def startup_event():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Tablas creadas automáticamente")

# Rutas
from app.api.v1.routes.dashboard import router as dashboard_router
app.include_router(dashboard_router, prefix="/api/v1", tags=["Dashboard"])

@app.get("/")
async def root():
    return {"message": "API Control de Horas - Practicantes", "status": "OK"}

@app.get("/health")
async def health():
    return {"status": "healthy"}