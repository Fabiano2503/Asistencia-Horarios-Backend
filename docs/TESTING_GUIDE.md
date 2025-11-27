# Guía de Testing de Endpoints - Sistema de Puntualidad

Esta guía te ayudará a testear todos los endpoints del sistema de puntualidad.

## 📋 Prerequisitos

1. **Servidor Django corriendo:**
   ```bash
   python manage.py runserver
   ```

2. **Base de datos migrada:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Datos de prueba (opcional):**
   - Practicantes activos en la base de datos
   - Estados de asistencia creados automáticamente

## 🧪 Métodos de Testing

### 1. Script Automatizado (Recomendado)

Ejecuta el script de Python que prueba todos los endpoints:

```bash
python test_endpoints.py
```

El script:
- ✅ Prueba todos los endpoints GET
- ✅ Prueba creación de justificaciones
- ✅ Prueba aprobar/rechazar justificaciones
- ✅ Muestra resultados con colores
- ✅ Genera un resumen final

### 2. Testing Manual con cURL

#### **GET /api/puntualidad/resumen/**
```bash
curl -X GET http://127.0.0.1:8000/api/puntualidad/resumen/
```

**Respuesta esperada:**
```json
{
  "asistencias": 0,
  "tardanzas": 0,
  "faltas": 0,
  "total": 0,
  "con_clases": 0,
  "ausentes_justificados": 0,
  "ausentes_sin_justificar": 0
}
```

#### **GET /api/puntualidad/alertas/**
```bash
curl -X GET http://127.0.0.1:8000/api/puntualidad/alertas/
```

**Respuesta esperada:** Array de alertas (puede estar vacío)

#### **GET /api/puntualidad/practicantes/**
```bash
curl -X GET http://127.0.0.1:8000/api/puntualidad/practicantes/
```

**Respuesta esperada:** Array de practicantes con su estado de asistencia

#### **GET /api/puntualidad/practicantes/activos/**
```bash
curl -X GET http://127.0.0.1:8000/api/puntualidad/practicantes/activos/
```

**Respuesta esperada:**
```json
[
  {
    "id": 1,
    "nombre": "Juan",
    "apellido": "Pérez",
    "nombre_completo": "Juan Pérez"
  }
]
```

#### **GET /api/puntualidad/justificaciones/**
```bash
curl -X GET http://127.0.0.1:8000/api/puntualidad/justificaciones/
```

**Respuesta esperada:** Array de justificaciones con información completa

#### **POST /api/puntualidad/justificaciones/crear/**
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

**Respuesta esperada (201):**
```json
{
  "mensaje": "Justificación creada exitosamente",
  "id": 1,
  "tickets_mes": 1,
  "tickets_max": 3,
  "sla_horas": 24,
  "tiene_evidencia": false
}
```

**Errores posibles:**
- `400`: Límite de tickets alcanzado (3/3)
- `400`: Datos inválidos
- `404`: Practicante no existe

#### **POST /api/puntualidad/justificaciones/{id}/aprobar/**
```bash
curl -X POST http://127.0.0.1:8000/api/puntualidad/justificaciones/1/aprobar/
```

**Respuesta esperada (200):**
```json
{
  "mensaje": "Justificación aprobada exitosamente",
  "id": 1,
  "estado": "aprobado"
}
```

#### **POST /api/puntualidad/justificaciones/{id}/rechazar/**
```bash
curl -X POST http://127.0.0.1:8000/api/puntualidad/justificaciones/1/rechazar/ \
  -H "Content-Type: application/json" \
  -d '{
    "motivo_rechazo": "Falta de evidencia"
  }'
```

**Respuesta esperada (200):**
```json
{
  "mensaje": "Justificación rechazada",
  "id": 1,
  "estado": "rechazado",
  "motivo_rechazo": "Falta de evidencia"
}
```

#### **GET /api/puntualidad/recuperaciones/**
```bash
curl -X GET http://127.0.0.1:8000/api/puntualidad/recuperaciones/
```

**Respuesta esperada:** Array de recuperaciones

### 3. Testing con Postman

1. Importa la colección de Postman (si está disponible)
2. O crea requests manualmente usando los ejemplos de cURL anteriores
3. Configura el ambiente con `BASE_URL = http://127.0.0.1:8000/api/puntualidad`

### 4. Testing desde el Frontend

1. Asegúrate de que `VITE_API_BASE_URL` apunte a `http://localhost:8000/api`
2. Inicia el frontend: `npm run dev`
3. Navega a la sección de Justificaciones
4. Prueba:
   - Crear nueva justificación
   - Aprobar justificación
   - Rechazar justificación

## 🔍 Validaciones a Probar

### Crear Justificación

1. **✅ Caso exitoso:**
   - Practicante activo existe
   - Fecha no es futura
   - Motivo tiene al menos 5 caracteres
   - No se ha alcanzado el límite de 3 tickets/mes

2. **❌ Casos de error:**
   - Practicante no existe → 400
   - Practicante inactivo → 400
   - Fecha futura → 400
   - Motivo muy corto (< 5 caracteres) → 400
   - Límite de tickets alcanzado (3/3) → 400

### Aprobar Justificación

1. **✅ Caso exitoso:**
   - Justificación existe
   - Justificación está en estado "pendiente"

2. **❌ Casos de error:**
   - Justificación no existe → 404
   - Justificación ya aprobada/rechazada → 400

### Rechazar Justificación

1. **✅ Caso exitoso:**
   - Justificación existe
   - Justificación está en estado "pendiente"
   - Motivo de rechazo proporcionado

2. **❌ Casos de error:**
   - Justificación no existe → 404
   - Motivo de rechazo vacío → 400
   - Justificación ya procesada → 400

## 📊 Estructura de la Base de Datos (ERD)

Según el ERD proporcionado:

- **practicante**: id, id_discord, nombre, apellido, correo, semestre
- **horario_clases**: id, practicante_id, dia_clase, dia_recuperacion
- **estado_asistencia**: id, estado
- **asistencia**: id, practicante_id, fecha, hora_entrada, hora_salida, estado_id, motivo
- **asistencia_recuperacion**: id, asistencia_id, fecha_recuperacion, hora_entrada, hora_salida, estado

## 🐛 Troubleshooting

### Error: "No se pudo conectar"
- Verifica que el servidor Django esté corriendo
- Verifica que la URL sea correcta (http://127.0.0.1:8000)

### Error: "OperationalError" o "Table doesn't exist"
- Ejecuta las migraciones: `python manage.py migrate`

### Error: "Practicante no existe"
- Crea practicantes de prueba en el admin de Django o mediante migraciones

### Error: "Límite de tickets alcanzado"
- Espera al siguiente mes o resetea los datos de prueba

## 📝 Notas

- Los estados de asistencia se crean automáticamente al usar los endpoints
- El límite de tickets es por mes calendario (1-31)
- El SLA es de 24 horas desde la creación de la justificación
- Las justificaciones rechazadas no cuentan para el límite de tickets

