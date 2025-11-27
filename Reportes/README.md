# Control de Horas - Practicantes  
**Backend Hexagonal + FastAPI + PostgreSQL + Docker**  

Sistema completo de control de horas, advertencias, permisos y reportes para practicantes.  

## Características ya implementadas y 100% funcionales

- Arquitectura Hexagonal (puertos y adaptadores) 
- Dashboard con resumen semanal (horas totales, faltantes, % cumplimiento)  
- Cálculo automático de horas trabajadas  
- Conteo de advertencias por practicante  
- Datos de prueba reales (7 practicantes + 28.5 horas + 2 advertencias)

## Cómo ejecutarlo 

### Opción 1: Con Docker (recomendado – funciona en cualquier máquina)

```bash
# 1. Clonar el repo
git clone <tu-repo>
cd practicantes-control-horas

# 2. Levantar todo (base de datos + API)
docker-compose up --build 