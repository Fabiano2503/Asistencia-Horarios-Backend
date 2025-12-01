# Módulo Puntualidad-Asistencia

Sistema de gestión de asistencia, puntualidad, justificaciones y recuperaciones de practicantes implementado con **Arquitectura Hexagonal (Ports and Adapters)**.

## 📋 Resumen

Este módulo gestiona el registro de asistencia diaria de practicantes, incluyendo:
- Control de puntualidad y asistencia
- Sistema de justificaciones con límite de tickets mensuales (máximo 3 por mes)
- Gestión de recuperaciones de horas
- Alertas automáticas de tardanzas y ausencias
- Resumen diario de asistencia

## 🚀 Tecnologías

- **Django 5.2.8** - Framework web
- **Django REST Framework** - API REST
- **Python 3.10+** - Lenguaje de programación
- **SQLite** - Base de datos (desarrollo)

## 📦 Instalación Rápida

```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## 🏗️ Arquitectura Hexagonal

El módulo implementa **Arquitectura Hexagonal** con separación de capas:

```
apps/puntualidad/
├── domain/              # Capa de Dominio (Núcleo)
│   ├── entities.py      # Entidades: Asistencia, EstadoAsistencia, HorarioClases
│   └── repositories.py  # Interfaces (Ports) de repositorios
│
├── application/          # Capa de Aplicación (Casos de Uso)
│   └── services.py      # Servicios: ResumenPuntualidadService, AlertasPuntualidadService, etc.
│
└── infrastructure/       # Capa de Infraestructura (Adapters)
    ├── models.py        # Modelos Django ORM
    ├── django_orm_repository.py  # Implementaciones de repositorios
    ├── serializers.py   # Serializers DRF
    └── views.py         # Controladores/Views
```

## 📱 Endpoints API

### Resumen y Alertas
- `GET /api/puntualidad/resumen/` - Resumen del día (asistencias, tardanzas, faltas)
- `GET /api/puntualidad/alertas/` - Alertas automáticas (tardanzas, ausencias, practicantes en riesgo)

### Practicantes
- `GET /api/puntualidad/practicantes/` - Lista de practicantes con estado de asistencia del día
- `GET /api/puntualidad/practicantes/activos/` - Lista de practicantes activos

### Justificaciones
- `GET /api/puntualidad/justificaciones/` - Listar todas las justificaciones
- `POST /api/puntualidad/justificaciones/crear/` - Crear nueva justificación
- `POST /api/puntualidad/justificaciones/{id}/aprobar/` - Aprobar justificación
- `POST /api/puntualidad/justificaciones/{id}/rechazar/` - Rechazar justificación

### Recuperaciones
- `GET /api/puntualidad/recuperaciones/` - Listar recuperaciones de horas

## 📝 Funcionalidades Principales

### 1. Sistema de Justificaciones
- **Límite de tickets**: Máximo 3 tickets por mes por practicante
- **SLA de 24 horas**: Tiempo máximo para revisar y aprobar justificaciones
- **Estados**: Pendiente, Aprobado, Rechazado, Vencido
- **Evidencia opcional**: Soporte para tickets de Trello o checklists

### 2. Alertas Automáticas
- **Tardanzas**: Detección automática con gracia de 5 minutos
- **Ausencias sin clase**: Identificación de ausencias sin horario registrado
- **Practicantes en riesgo**: Alerta cuando un practicante alcanza 3 ausencias sin justificar en el mes

### 3. Gestión de Recuperaciones
- Registro de horas de recuperación
- Estados: Programado, En Progreso, Completado, Cancelado
- Cálculo automático de horas completadas

## 📝 Cambios Realizados

### Refactorización con Arquitectura Hexagonal

1. **Separación de Capas:**
   - **Domain**: Entidades de negocio independientes de frameworks
   - **Application**: Servicios que implementan casos de uso
   - **Infrastructure**: Implementaciones con Django ORM

2. **Servicios Implementados:**
   - `ResumenPuntualidadService` - Genera resumen diario de asistencia
   - `AlertasPuntualidadService` - Genera alertas automáticas
   - `ListarPracticantesPuntualidadService` - Lista practicantes con estado
   - `ListarJustificacionesService` - Gestiona justificaciones
   - `CrearJustificacionService` - Crea nuevas justificaciones
   - `AprobarJustificacionService` - Aprueba justificaciones
   - `RechazarJustificacionService` - Rechaza justificaciones
   - `ListarRecuperacionesService` - Gestiona recuperaciones

3. **Repositorios:**
   - Interfaces definidas en `domain/repositories.py`
   - Implementaciones en `infrastructure/django_orm_repository.py`

### Beneficios Obtenidos

- ✅ **Testabilidad**: Fácil crear mocks de repositorios para testing
- ✅ **Mantenibilidad**: Separación clara de responsabilidades
- ✅ **Escalabilidad**: Fácil cambiar implementaciones sin afectar el dominio
- ✅ **Independencia**: La lógica de negocio no depende de Django

## 🔧 Configuración

Crea un archivo `.env` en la carpeta `backend/`:

```env
SECRET_KEY=tu-secret-key-aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```
