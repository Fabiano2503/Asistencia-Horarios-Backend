# 🐍 Backend - Sistema de Asistencia y Horarios

Backend desarrollado con Django REST Framework para gestionar asistencias, justificaciones y recuperaciones de practicantes.

## 📁 Estructura del Proyecto

```
backend/
├── apps/                    # Aplicaciones Django
│   ├── bot_discord/        # Integración con Discord
│   ├── practicantes/       # Gestión de practicantes
│   └── puntualidad/        # Sistema de puntualidad y justificaciones
├── config/                 # Configuración de Django
├── docs/                   # Documentación
├── scripts/                # Scripts de utilidad y testing
├── manage.py              # Script de administración de Django
└── requirements.txt       # Dependencias Python
```

## 🚀 Instalación Rápida

### 1. Crear y activar entorno virtual

```bash
cd backend
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Configurar variables de entorno

Crea un archivo `.env` en la raíz de `backend/`:

```env
SECRET_KEY=tu-secret-key-aqui
DEBUG=True
REDIS_HOST=127.0.0.1
REDIS_PORT=6379
```

O copia la plantilla:
```bash
cp .env.example .env
# Luego edita .env con tus valores
```

### 4. Aplicar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Ejecutar servidor

```bash
python manage.py runserver
```

O usa los scripts de inicio:
- **Windows:** `start.bat`
- **Linux/Mac:** `./start.sh`

El servidor estará disponible en: `http://127.0.0.1:8000`

## 📡 Endpoints API

**Base URL:** `http://127.0.0.1:8000/api/puntualidad/`

### Principales Endpoints

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/resumen/` | Resumen de asistencia del día |
| GET | `/alertas/` | Alertas automáticas |
| GET | `/practicantes/` | Lista de practicantes con estado |
| GET | `/practicantes/activos/` | Practicantes activos |
| GET | `/justificaciones/` | Lista de justificaciones |
| POST | `/justificaciones/crear/` | Crear nueva justificación |
| POST | `/justificaciones/{id}/aprobar/` | Aprobar justificación |
| POST | `/justificaciones/{id}/rechazar/` | Rechazar justificación |
| GET | `/recuperaciones/` | Lista de recuperaciones |

**Ver [docs/ENDPOINTS.md](./docs/ENDPOINTS.md) para la lista completa de 22 endpoints.**

## 🧪 Testing

### Verificar Backend

```bash
python scripts/check_backend.py
```

### Testing Automatizado

```bash
python scripts/test_endpoints.py
```

**Ver [docs/TESTING_GUIDE.md](./docs/TESTING_GUIDE.md) para más información.**

## 🔧 Configuración

### Redis (para Channels/WebSockets)

El sistema usa Redis para Django Channels:

```bash
# Iniciar Redis
redis-server
```

### CORS

El backend está configurado para aceptar requests del frontend. Verifica `config/settings.py` para ajustar `CORS_ALLOWED_ORIGINS`.

## 📚 Documentación

- **[docs/ENDPOINTS.md](./docs/ENDPOINTS.md)** - Lista completa de endpoints
- **[docs/TESTING_GUIDE.md](./docs/TESTING_GUIDE.md)** - Guía de testing
- **[ARCHIVOS_A_SUBIR.md](./ARCHIVOS_A_SUBIR.md)** - Qué archivos subir a GitHub

## 🛠️ Comandos Útiles

```bash
# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Ejecutar servidor
python manage.py runserver

# Acceder al admin
python manage.py createsuperuser
# Luego: http://127.0.0.1:8000/admin

# Shell de Django
python manage.py shell

# Verificar backend
python scripts/check_backend.py
```

## 🚀 Para GitHub

**Ver [ARCHIVOS_A_SUBIR.md](./ARCHIVOS_A_SUBIR.md) para instrucciones completas.**

Resumen rápido:
```bash
cd backend
git init
git add .
git commit -m "Backend Django - Sistema de Asistencia y Horarios"
git remote add origin https://github.com/tu-usuario/tu-repo.git
git push -u origin main
```

## 🔐 Seguridad

- **SECRET_KEY**: No compartir en producción
- **DEBUG**: Desactivar en producción
- **ALLOWED_HOSTS**: Configurar en producción
- **CORS**: Configurar orígenes permitidos

## 📝 Notas

- El sistema crea automáticamente los estados de asistencia al usar los endpoints
- El límite de tickets es de 3 por mes por practicante
- El SLA para revisar justificaciones es de 24 horas

---

**✅ El backend está completamente organizado y listo para usar.**
