# 📤 Archivos a Subir a GitHub

## ✅ Archivos ESENCIALES (SÍ subir)

### Código Fuente
- ✅ `apps/` - Todas las aplicaciones Django (código fuente)
- ✅ `config/` - Configuración de Django
- ✅ `manage.py` - Script principal de Django

### Documentación Principal
- ✅ `README.md` - **Documentación principal del proyecto** (ESENCIAL)
- ✅ `docs/ENDPOINTS.md` - Lista completa de endpoints
- ✅ `docs/TESTING_GUIDE.md` - Guía de testing

### Scripts
- ✅ `scripts/` - Scripts de utilidad (check_backend.py, test_endpoints.py, etc.)
- ✅ `start.bat` / `start.sh` - Scripts de inicio

### Configuración
- ✅ `requirements.txt` - Dependencias Python (ESENCIAL)
- ✅ `.gitignore` - Archivos a ignorar (ESENCIAL)
- ✅ `.env.example` - Plantilla de variables de entorno

### READMEs de Apps (opcionales pero útiles)
- ✅ `apps/bot_discord/README.md` - Documentación del módulo bot
- ✅ `apps/practicantes/README.md` - Documentación del módulo practicantes

---

## ❌ Archivos NO ESENCIALES (puedes eliminar antes de subir)

### Documentación Redundante
- ❌ `QUÉ_SUBIR_A_GITHUB.md` - Este archivo (ya no necesario después de leerlo)
- ❌ `ORGANIZACIÓN_COMPLETA.md` - Redundante
- ❌ `RESUMEN_ORGANIZACIÓN.md` - Redundante
- ❌ `ESTRUCTURA.md` - Puede ser útil, pero no esencial

### Archivos que NO se Suben (gracias a .gitignore)
- ❌ `db.sqlite3` - Base de datos local
- ❌ `__pycache__/` - Archivos compilados
- ❌ `.env` - Variables de entorno con secretos
- ❌ `venv/` - Entorno virtual

---

## 📋 Resumen: Mínimo Necesario

**Para que el proyecto funcione en GitHub, necesitas MÍNIMO:**

1. ✅ `README.md` - Documentación principal
2. ✅ `requirements.txt` - Dependencias
3. ✅ `.gitignore` - Archivos a ignorar
4. ✅ `manage.py` - Script principal
5. ✅ `apps/` - Código fuente
6. ✅ `config/` - Configuración
7. ✅ `docs/ENDPOINTS.md` - Documentación de API (recomendado)

**Todo lo demás es opcional pero recomendado.**

---

## 🚀 Comando para Subir

```bash
cd backend
git init
git add .
git commit -m "Backend Django - Sistema de Asistencia y Horarios"
git remote add origin https://github.com/tu-usuario/tu-repo.git
git push -u origin main
```

**Nota:** Git automáticamente ignorará los archivos en `.gitignore`, así que no te preocupes por `db.sqlite3`, `__pycache__/`, etc.
