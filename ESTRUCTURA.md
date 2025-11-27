# 📁 Estructura del Backend

## Organización del Proyecto

```
backend/
├── apps/                          # Aplicaciones Django
│   ├── bot_discord/              # Integración con Discord
│   ├── practicantes/             # Gestión de practicantes
│   └── puntualidad/              # Sistema de puntualidad y justificaciones
│
├── config/                        # Configuración de Django
│   ├── settings.py               # Configuración principal
│   ├── urls.py                   # URLs principales
│   ├── views.py                  # Vista raíz de la API
│   ├── asgi.py                   # Configuración ASGI (Channels)
│   └── wsgi.py                   # Configuración WSGI
│
├── docs/                          # Documentación
│   ├── ENDPOINTS.md              # Documentación completa de endpoints
│   ├── TESTING_GUIDE.md          # Guía de testing
│   ├── README_TESTING.md         # Resumen de testing
│   ├── README_TEST_ENDPOINTS.md  # Testing de endpoints
│   └── test_endpoints.html       # Interfaz HTML para testing
│
├── scripts/                       # Scripts de utilidad
│   ├── check_backend.py          # Verificación del backend
│   ├── test_endpoints.py         # Testing automatizado de endpoints
│   ├── verify_database_structure.py  # Verificación de estructura BD
│   ├── test_endpoints.ps1        # Script PowerShell para testing
│   └── test_endpoints.sh         # Script Bash para testing
│
├── manage.py                      # Script de administración Django
├── requirements.txt               # Dependencias Python
│
├── README.md                      # Documentación principal
├── GITHUB_SETUP.md               # Guía para subir a GitHub
├── README_GITHUB.md              # Verificación para GitHub
├── ESTRUCTURA.md                 # Este archivo
│
├── start.bat                      # Script de inicio (Windows)
└── start.sh                       # Script de inicio (Linux/Mac)
```

## 📂 Descripción de Carpetas

### `apps/`
Contiene todas las aplicaciones Django del proyecto:
- **bot_discord**: Integración con Discord Bot
- **practicantes**: Gestión de practicantes (CRUD)
- **puntualidad**: Sistema de puntualidad, justificaciones y recuperaciones

### `config/`
Configuración central de Django:
- **settings.py**: Configuración principal (base de datos, apps, middleware, etc.)
- **urls.py**: Rutas principales del proyecto
- **views.py**: Vista raíz que devuelve información básica de la API
- **asgi.py**: Configuración para Django Channels (WebSockets)
- **wsgi.py**: Configuración WSGI estándar

### `docs/`
Documentación del proyecto:
- **ENDPOINTS.md**: Lista completa de todos los endpoints con ejemplos
- **TESTING_GUIDE.md**: Guía detallada de testing
- **test_endpoints.html**: Interfaz HTML interactiva para probar endpoints

### `scripts/`
Scripts de utilidad y testing:
- **check_backend.py**: Verifica que el backend esté configurado correctamente
- **test_endpoints.py**: Testing automatizado de todos los endpoints
- **verify_database_structure.py**: Verifica que la estructura de BD coincida con el ERD

## 📋 Archivos Importantes

### Archivos de Configuración
- `manage.py`: Script principal de Django
- `requirements.txt`: Lista de dependencias Python
- `.gitignore`: Archivos a ignorar en Git
- `.env.example`: Plantilla de variables de entorno (crear manualmente)

### Scripts de Inicio
- `start.bat`: Inicia el servidor en Windows
- `start.sh`: Inicia el servidor en Linux/Mac

### Documentación
- `README.md`: Documentación principal del backend
- `GITHUB_SETUP.md`: Guía para subir a GitHub
- `ESTRUCTURA.md`: Este archivo

## 🚫 Archivos que NO se suben a GitHub

Gracias al `.gitignore`, estos archivos NO se suben:
- `db.sqlite3`: Base de datos local
- `venv/` o `env/`: Entorno virtual
- `__pycache__/`: Archivos compilados de Python
- `*.pyc`: Archivos compilados
- `.env`: Variables de entorno con secretos
- `*.log`: Archivos de log

## ✅ Archivos que SÍ se suben a GitHub

- Todo el código fuente (`apps/`, `config/`)
- `manage.py`
- `requirements.txt`
- Archivos de documentación (`docs/`, `README.md`, etc.)
- Scripts de utilidad (`scripts/`)
- Scripts de inicio (`start.bat`, `start.sh`)
- `.gitignore`
- `.env.example` (plantilla sin secretos)

## 🔄 Flujo de Trabajo

1. **Desarrollo**: Trabajar en `apps/` y `config/`
2. **Testing**: Usar scripts en `scripts/`
3. **Documentación**: Actualizar archivos en `docs/`
4. **Deploy**: Subir solo la carpeta `backend/` a GitHub

## 📝 Notas

- El backend es completamente independiente del frontend
- No necesitas el frontend para que el backend funcione
- Todos los endpoints están documentados en `docs/ENDPOINTS.md`
- Los scripts de testing están en `scripts/`



