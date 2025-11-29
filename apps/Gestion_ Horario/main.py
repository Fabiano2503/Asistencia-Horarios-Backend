# main.py
from fastapi import FastAPI
from gestion_horario.infrastructure.urls import router

app = FastAPI(
    title="Gestión de Horarios - Practicantes",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Backend Horarios Practicantes - 100% funcional"}