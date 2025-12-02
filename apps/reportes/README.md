# Control de Horas - Practicantes  
**Backend Hexagonal  PostgreSQL + Docker**  

Sistema completo de control de horas, advertencias, permisos y reportes para practicantes.  
¡Exactamente igual a la pantalla que nos pasaron!

## Características ya implementadas y 100% funcionales

- Arquitectura Hexagonal (puertos y adaptadores) – limpia y profesional  
- Dashboard con resumen semanal (horas totales, faltantes, % cumplimiento)  
- Cálculo automático de horas trabajadas  
- Conteo de advertencias por practicante  
- Base de datos PostgreSQL con tablas reales  
- Swagger UI interactivo: http://localhost:8000/docs  
- ReDoc bonito: http://localhost:8000/redoc  
- Todo dockerizado – cero configuración en Windows/Mac/Linux  
- Creación automática de tablas al iniciar  
- Datos de prueba reales (7 practicantes + 28.5 horas + 2 advertencias)

## Cómo ejecutarlo (2 minutos – funciona siempre)

### Opción 1: Con Docker (recomendado – funciona en cualquier máquina)

```bash
# 1. Clonar el repo
git clone <tu-repo>
cd practicantes-control-horas

# 2. Levantar todo (base de datos + API)
docker-compose up --build