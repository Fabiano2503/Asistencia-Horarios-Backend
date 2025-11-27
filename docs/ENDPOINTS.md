# 🔗 Documentación de Endpoints - API REST

## 📍 Información General

**Servidor Local:** `http://127.0.0.1:8000`  
**API Base:** `http://127.0.0.1:8000/api`  
**Versión:** 1.0.0

---

## 📋 Índice

1. [Endpoint Raíz](#-endpoint-raíz)
2. [Endpoints de Puntualidad](#-endpoints-de-puntualidad)
3. [Endpoints de Practicantes](#-endpoints-de-practicantes)
4. [Endpoints de Bot Discord](#-endpoints-de-bot-discord)
5. [Endpoints de Administración](#-endpoints-de-administración)
6. [Ejemplos de Uso](#-ejemplos-de-uso)
7. [Probar en el Navegador](#-probar-en-el-navegador)
8. [Checklist de Verificación](#-checklist-de-verificación)
9. [Códigos de Estado HTTP](#-códigos-de-estado-http)
10. [Notas Importantes](#-notas-importantes)
11. [Herramientas para Probar](#-herramientas-para-probar)

---

## 🏠 Endpoint Raíz

### GET `/`

Información básica de la API.

**URL Completa:** `http://127.0.0.1:8000/`

**Respuesta:**
```json
{
  "status": "ok",
  "api": "Sistema de Asistencia y Horarios",
  "version": "1.0.0"
}
```

**Estado Esperado:** `200 OK`

---

## 📊 Endpoints de Puntualidad

**Base URL:** `http://127.0.0.1:8000/api/puntualidad/`

### GET Endpoints

#### 1. Resumen de Puntualidad
- **Endpoint:** `GET /api/puntualidad/resumen/`
- **URL Completa:** `http://127.0.0.1:8000/api/puntualidad/resumen/`
- **Descripción:** Resumen de asistencia del día
- **Estado Esperado:** `200 OK`

#### 2. Alertas Automáticas
- **Endpoint:** `GET /api/puntualidad/alertas/`
- **URL Completa:** `http://127.0.0.1:8000/api/puntualidad/alertas/`
- **Descripción:** Alertas automáticas del sistema
- **Estado Esperado:** `200 OK`

#### 3. Lista de Practicantes
- **Endpoint:** `GET /api/puntualidad/practicantes/`
- **URL Completa:** `http://127.0.0.1:8000/api/puntualidad/practicantes/`
- **Descripción:** Lista de practicantes con estado de asistencia
- **Estado Esperado:** `200 OK`

#### 4. Practicantes Activos
- **Endpoint:** `GET /api/puntualidad/practicantes/activos/`
- **URL Completa:** `http://127.0.0.1:8000/api/puntualidad/practicantes/activos/`
- **Descripción:** Lista de practicantes activos (para formularios)
- **Estado Esperado:** `200 OK`

#### 5. Lista de Justificaciones
- **Endpoint:** `GET /api/puntualidad/justificaciones/`
- **URL Completa:** `http://127.0.0.1:8000/api/puntualidad/justificaciones/`
- **Descripción:** Lista de todas las justificaciones
- **Estado Esperado:** `200 OK`

#### 6. Lista de Recuperaciones
- **Endpoint:** `GET /api/puntualidad/recuperaciones/`
- **URL Completa:** `http://127.0.0.1:8000/api/puntualidad/recuperaciones/`
- **Descripción:** Lista de todas las recuperaciones
- **Estado Esperado:** `200 OK`

### POST Endpoints

#### 7. Crear Justificación
- **Endpoint:** `POST /api/puntualidad/justificaciones/crear/`
- **URL Completa:** `http://127.0.0.1:8000/api/puntualidad/justificaciones/crear/`
- **Descripción:** Crear nueva justificación
- **Estado Esperado:** `201 Created`
- **Body (JSON):**
  ```json
  {
    "practicante_id": 1,
    "fecha": "2024-01-15",
    "motivo": "Enfermedad",
    "tiene_evidencia": false,
    "ticket_id": "TKT-123"
  }
  ```

#### 8. Aprobar Justificación
- **Endpoint:** `POST /api/puntualidad/justificaciones/{id}/aprobar/`
- **URL Completa:** `http://127.0.0.1:8000/api/puntualidad/justificaciones/{id}/aprobar/`
- **Descripción:** Aprobar una justificación
- **Estado Esperado:** `200 OK`
- **Nota:** Reemplaza `{id}` con el ID numérico (ej: `1`, `2`, `3`)

#### 9. Rechazar Justificación
- **Endpoint:** `POST /api/puntualidad/justificaciones/{id}/rechazar/`
- **URL Completa:** `http://127.0.0.1:8000/api/puntualidad/justificaciones/{id}/rechazar/`
- **Descripción:** Rechazar una justificación
- **Estado Esperado:** `200 OK`
- **Body (JSON):**
  ```json
  {
    "motivo_rechazo": "Falta de evidencia"
  }
  ```
- **Nota:** Reemplaza `{id}` con el ID numérico (ej: `1`, `2`, `3`)

---

## 👥 Endpoints de Practicantes

**Base URL:** `http://127.0.0.1:8000/api/practicantes/`

#### 10. Lista de Practicantes
- **Endpoint:** `GET /api/practicantes/`
- **URL Completa:** `http://127.0.0.1:8000/api/practicantes/`
- **Descripción:** Obtener lista de practicantes
- **Estado Esperado:** `200 OK`

#### 11. Crear Practicante
- **Endpoint:** `POST /api/practicantes/`
- **URL Completa:** `http://127.0.0.1:8000/api/practicantes/`
- **Descripción:** Crear nuevo practicante
- **Estado Esperado:** `201 Created`

#### 12. Obtener Practicante por ID
- **Endpoint:** `GET /api/practicantes/{id}/`
- **URL Completa:** `http://127.0.0.1:8000/api/practicantes/{id}/`
- **Descripción:** Obtener practicante por ID
- **Estado Esperado:** `200 OK`
- **Nota:** Reemplaza `{id}` con el ID numérico

#### 13. Actualizar Practicante
- **Endpoint:** `PUT /api/practicantes/{id}/`
- **URL Completa:** `http://127.0.0.1:8000/api/practicantes/{id}/`
- **Descripción:** Actualizar practicante
- **Estado Esperado:** `200 OK`
- **Nota:** Reemplaza `{id}` con el ID numérico

#### 14. Eliminar Practicante
- **Endpoint:** `DELETE /api/practicantes/{id}/`
- **URL Completa:** `http://127.0.0.1:8000/api/practicantes/{id}/`
- **Descripción:** Eliminar practicante
- **Estado Esperado:** `204 No Content`
- **Nota:** Reemplaza `{id}` con el ID numérico

#### 15. Estadísticas de Practicantes
- **Endpoint:** `GET /api/practicantes/stats/`
- **URL Completa:** `http://127.0.0.1:8000/api/practicantes/stats/`
- **Descripción:** Obtener estadísticas de practicantes
- **Estado Esperado:** `200 OK`

---

## 🤖 Endpoints de Bot Discord

**Base URL:** `http://127.0.0.1:8000/api/bot/`

#### 16. Métricas del Bot
- **Endpoint:** `GET /api/bot/metrics/`
- **URL Completa:** `http://127.0.0.1:8000/api/bot/metrics/`
- **Descripción:** Obtener métricas del bot
- **Estado Esperado:** `200 OK`

#### 17. Estado del Bot
- **Endpoint:** `GET /api/bot/status/`
- **URL Completa:** `http://127.0.0.1:8000/api/bot/status/`
- **Descripción:** Obtener estado del bot
- **Estado Esperado:** `200 OK`

#### 18. Actualizar Estado del Bot
- **Endpoint:** `POST /api/bot/status/`
- **URL Completa:** `http://127.0.0.1:8000/api/bot/status/`
- **Descripción:** Actualizar estado del bot
- **Estado Esperado:** `200 OK`

#### 19. Resumen del Bot
- **Endpoint:** `GET /api/bot/resumen/`
- **URL Completa:** `http://127.0.0.1:8000/api/bot/resumen/`
- **Descripción:** Obtener resumen del bot
- **Estado Esperado:** `200 OK`

#### 20. Estado Detallado del Bot
- **Endpoint:** `GET /api/bot/estado/`
- **URL Completa:** `http://127.0.0.1:8000/api/bot/estado/`
- **Descripción:** Obtener estado detallado del bot
- **Estado Esperado:** `200 OK`

#### 21. Lista de Servidores
- **Endpoint:** `GET /api/bot/servers/`
- **URL Completa:** `http://127.0.0.1:8000/api/bot/servers/`
- **Descripción:** Obtener lista de servidores del bot
- **Estado Esperado:** `200 OK`

---

## 🔧 Endpoints de Administración

#### 22. Panel de Administración Django
- **Endpoint:** `GET /admin/`
- **URL Completa:** `http://127.0.0.1:8000/admin/`
- **Descripción:** Panel de administración de Django
- **Estado Esperado:** `200 OK` (requiere login)

---

## 📝 Ejemplos de Uso

### Ejemplo 1: Obtener Resumen de Puntualidad
```bash
curl http://127.0.0.1:8000/api/puntualidad/resumen/
```

### Ejemplo 2: Crear Justificación
```bash
curl -X POST http://127.0.0.1:8000/api/puntualidad/justificaciones/crear/ \
  -H "Content-Type: application/json" \
  -d '{
    "practicante_id": 1,
    "fecha": "2024-01-15",
    "motivo": "Enfermedad",
    "tiene_evidencia": false,
    "ticket_id": "TKT-123"
  }'
```

### Ejemplo 3: Aprobar Justificación (ID = 1)
```bash
curl -X POST http://127.0.0.1:8000/api/puntualidad/justificaciones/1/aprobar/
```

### Ejemplo 4: Rechazar Justificación (ID = 1)
```bash
curl -X POST http://127.0.0.1:8000/api/puntualidad/justificaciones/1/rechazar/ \
  -H "Content-Type: application/json" \
  -d '{
    "motivo_rechazo": "Falta de evidencia"
  }'
```

### Ejemplo 5: Obtener Practicantes Activos
```bash
curl http://127.0.0.1:8000/api/puntualidad/practicantes/activos/
```

### Ejemplo 6: Obtener Lista de Justificaciones
```bash
curl http://127.0.0.1:8000/api/puntualidad/justificaciones/
```

### Ejemplo 7: Obtener Lista de Recuperaciones
```bash
curl http://127.0.0.1:8000/api/puntualidad/recuperaciones/
```

---

## 🌐 Probar en el Navegador

Puedes probar los endpoints GET directamente en tu navegador haciendo clic en los siguientes enlaces:

### Endpoints GET (Click para abrir)

1. [🏠 Página Principal](http://127.0.0.1:8000/)
2. [Resumen de Puntualidad](http://127.0.0.1:8000/api/puntualidad/resumen/)
3. [Alertas](http://127.0.0.1:8000/api/puntualidad/alertas/)
4. [Practicantes](http://127.0.0.1:8000/api/puntualidad/practicantes/)
5. [Practicantes Activos](http://127.0.0.1:8000/api/puntualidad/practicantes/activos/)
6. [Justificaciones](http://127.0.0.1:8000/api/puntualidad/justificaciones/)
7. [Recuperaciones](http://127.0.0.1:8000/api/puntualidad/recuperaciones/)
8. [Métricas del Bot](http://127.0.0.1:8000/api/bot/metrics/)
9. [Estado del Bot](http://127.0.0.1:8000/api/bot/status/)
10. [Resumen del Bot](http://127.0.0.1:8000/api/bot/resumen/)
11. [Servidores del Bot](http://127.0.0.1:8000/api/bot/servers/)

---

## ✅ Checklist de Verificación

Usa esta lista para verificar que todos los endpoints funcionen correctamente:

### Puntualidad
- [ ] GET `/api/puntualidad/resumen/`
- [ ] GET `/api/puntualidad/alertas/`
- [ ] GET `/api/puntualidad/practicantes/`
- [ ] GET `/api/puntualidad/practicantes/activos/`
- [ ] GET `/api/puntualidad/justificaciones/`
- [ ] POST `/api/puntualidad/justificaciones/crear/`
- [ ] POST `/api/puntualidad/justificaciones/{id}/aprobar/`
- [ ] POST `/api/puntualidad/justificaciones/{id}/rechazar/`
- [ ] GET `/api/puntualidad/recuperaciones/`

### Practicantes
- [ ] GET `/api/practicantes/`
- [ ] POST `/api/practicantes/`
- [ ] GET `/api/practicantes/{id}/`
- [ ] PUT `/api/practicantes/{id}/`
- [ ] DELETE `/api/practicantes/{id}/`
- [ ] GET `/api/practicantes/stats/`

### Bot Discord
- [ ] GET `/api/bot/metrics/`
- [ ] GET `/api/bot/status/`
- [ ] POST `/api/bot/status/`
- [ ] GET `/api/bot/resumen/`
- [ ] GET `/api/bot/estado/`
- [ ] GET `/api/bot/servers/`

---

## 🔍 Códigos de Estado HTTP

| Código | Significado | Descripción |
|--------|-------------|-------------|
| 200 | OK | Solicitud exitosa |
| 201 | Created | Recurso creado exitosamente |
| 204 | No Content | Solicitud exitosa sin contenido |
| 400 | Bad Request | Datos inválidos o mal formados |
| 404 | Not Found | Recurso no encontrado |
| 500 | Internal Server Error | Error del servidor |

---

## 📌 Notas Importantes

1. **Servidor debe estar corriendo:** Asegúrate de ejecutar `python manage.py runserver` antes de probar los endpoints

2. **CORS:** El backend está configurado para aceptar requests del frontend en desarrollo

3. **Content-Type:** Para POST/PUT, usar `Content-Type: application/json`

4. **IDs:** Reemplazar `{id}` con números reales (ej: `1`, `2`, `3`)

5. **Autenticación:** Algunos endpoints pueden requerir autenticación en producción

6. **Variables de Entorno:** Configurar `.env` con las variables necesarias (REDIS_HOST, REDIS_PORT, etc.)

7. **Base de Datos:** Asegúrate de ejecutar `python manage.py migrate` antes de usar los endpoints

---

## 🛠️ Herramientas para Probar

### Navegador
- Para endpoints GET, puedes abrirlos directamente en el navegador

### cURL
- Herramienta de línea de comandos para probar todos los métodos HTTP
- Ejemplo: `curl http://127.0.0.1:8000/api/puntualidad/resumen/`

### Postman
- Aplicación para testing completo de APIs
- Permite guardar colecciones y entornos

### Thunder Client
- Extensión de VS Code para probar endpoints
- Interfaz similar a Postman

### Scripts de Testing
- `scripts/test_endpoints.py` - Script automatizado de testing
- `test_endpoints.html` - Interfaz HTML interactiva para probar endpoints

---

## 📚 Documentación Adicional

- **Backend README:** `../README.md`
- **Guía de Testing:** `TESTING_GUIDE.md`
- **Setup para GitHub:** `../GITHUB_SETUP.md`

---

**Última actualización:** 2024-11-27  
**Total de Endpoints:** 22



