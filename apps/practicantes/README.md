# Módulo de Practicantes

Este módulo gestiona la información de los practicantes.

## Endpoints

### Listar y Filtrar Practicantes

- **GET /api/practicantes/**
- **Query Params:**
  - `nombre` (string): Filtra por nombre.
  - `correo` (string): Filtra por correo electrónico.
  - `estado` (string): Filtra por estado (`activo`, `en_recuperacion`, `en_riesgo`).
- **Respuesta:**
  ```json
  {
    "count": 100,
    "next": "https://IP:PUERTO/api/practicantes/?page=2",
    "previous": null,
    "results": [
      {
        "id": 1,
        "id_discord": 123456789012345678,
        "nombre": "string",
        "apellido": "string",
        "correo": "user1@correo.com",
        "semestre": 4,
        "estado": "activo"
      },
      {
        "id": 2,
        "id_discord": 123456789012345679,
        "nombre": "string",
        "apellido": "string",
        "correo": "user2@correo.com",
        "semestre": 5,
        "estado": "activo"
      },
      {
        "id": 3,
        "id_discord": 123456789012345670,
        "nombre": "string",
        "apellido": "string",
        "correo": "user3@correo.com",
        "semestre": 6,
        "estado": "activo"
      },
      {
        "id": 4,
        "id_discord": 123456789012345671,
        "nombre": "string",
        "apellido": "string",
        "correo": "user4@correo.com",
        "semestre": 6,
        "estado": "activo"
      },
      {
        "id": 5,
        "id_discord": 123456789012345672,
        "nombre": "string",
        "apellido": "string",
        "correo": "user5@correo.com",
        "semestre": 5,
        "estado": "en_recuperacion"
      },
      {
        "id": 6,
        "id_discord": 123456789012345673,
        "nombre": "string",
        "apellido": "string",
        "correo": "user6@correo.com",
        "semestre": 4,
        "estado": "activo"
      }
    ]
  }
  ```

### Obtener Detalle de un Practicante

- **GET /api/practicantes/{id}/**

### Crear un Practicante

- **POST /api/practicantes/**
- **Body:**
  ```json
  {
    "id_discord": 123456789012345678,
    "nombre": "string",
    "apellido": "string",
    "correo": "user@correo.com",
    "semestre": 4,
    "estado": "activo"
  }
  ```

### Actualizar un Practicante

- **PUT /api/practicantes/{id}/**
- **PATCH /api/practicantes/{id}/**
- **Body:** (similar al de creación)

### Eliminar un Practicante

- **DELETE /api/practicantes/{id}/**

### Obtener Estadísticas

- **GET /api/practicantes/estadisticas/**
- **Respuesta:**
  ```json
  {
    "total": 0,
    "activos": 0,
    "en_recuperacion": 0,
    "en_riesgo": 0
  }
  ```

## Endpoints del Dashboard del Practicante

### Vista de Inicio

- **GET /api/practicantes/dashboard/inicio/**
- **Query Params:**
  - `practicante_id` (integer, opcional): ID del practicante (por defecto: 1)
- **Respuesta:**
  ```json
  {
    "mensaje": "Bienvenido/a - Inicio Práctica",
    "practicante_id": 1
  }
  ```

### Mi Asistencia

#### Listar Asistencias

- **GET /api/practicantes/dashboard/mi-asistencia/**
- **Query Params:**
  - `practicante_id` (integer, opcional): ID del practicante (por defecto: 1)
- **Respuesta:**
  ```json
  [
    {
      "id": 1,
      "practicante_id": 1,
      "fecha": "2025-11-27",
      "hora_entrada": "08:00:00",
      "hora_salida": null
    }
  ]
  ```

#### Registrar Asistencia

- **POST /api/practicantes/dashboard/mi-asistencia/**
- **Body:**
  ```json
  {
    "practicante_id": 1,
    "fecha": "2025-11-27",
    "hora_entrada": "08:00:00",
    "hora_salida": "17:00:00"
  }
  ```

### Mi Horario

#### Listar Horarios

- **GET /api/practicantes/dashboard/mi-horario/**
- **Query Params:**
  - `practicante_id` (integer, opcional): ID del practicante (por defecto: 1)
- **Respuesta:**
  ```json
  [
    {
      "id": 1,
      "practicante_id": 1,
      "dia_semana": "lunes",
      "hora_inicio": "08:00:00",
      "hora_fin": "17:00:00"
    }
  ]
  ```

#### Registrar Horario

- **POST /api/practicantes/dashboard/mi-horario/**
- **Body:**
  ```json
  {
    "practicante_id": 1,
    "dia_semana": "lunes",
    "hora_inicio": "08:00:00",
    "hora_fin": "17:00:00"
  }
  ```

### Calendario Semanal

#### Ver Calendario Semanal

- **GET /api/practicantes/dashboard/calendario-semanal/**
- **Query Params:**
  - `practicante_id` (integer, opcional): ID del practicante (por defecto: 1)
- **Respuesta:**
  ```json
  [
    {
      "fecha": "2025-11-24",
      "dia_semana": "lunes",
      "trabajó": false,
      "horas_trabajadas": 0.0
    },
    {
      "fecha": "2025-11-25",
      "dia_semana": "martes",
      "trabajó": true,
      "horas_trabajadas": 5.0
    }
  ]
  ```

### Estadísticas Personales

#### Ver Estadísticas de la Semana

- **GET /api/practicantes/dashboard/estadisticas-personales/**
- **Query Params:**
  - `practicante_id` (integer, opcional): ID del practicante (por defecto: 1)
- **Respuesta:**
  ```json
  {
    "semana_actual": {
      "inicio": "2025-11-24",
      "fin": "2025-11-30"
    },
    "dias_trabajados": 1,
    "dias_con_asistencia_completa": 1,
    "total_horas_semana": 5.0,
    "promedio_horas_diario": 5.0,
    "dias_semana_total": 7
  }
  ```

### Seguimiento Disciplinario

#### Ver Advertencias

- **GET /api/practicantes/dashboard/advertencias/**
- **Query Params:**
  - `practicante_id` (integer, opcional): ID del practicante (por defecto: 1)
- **Respuesta:**
  ```json
  [
    {
      "id": 1,
      "practicante_id": 1,
      "tipo": "retraso",
      "gravedad": "leve",
      "descripcion": "Llegó 15 minutos tarde el lunes",
      "fecha": "2025-11-24",
      "resuelta": true,
      "fecha_resolucion": null
    }
  ]
  ```

#### Ver Estadísticas de Advertencias

- **GET /api/practicantes/dashboard/advertencias/estadisticas/**
- **Query Params:**
  - `practicante_id` (integer, opcional): ID del practicante (por defecto: 1)
- **Respuesta:**
  ```json
  {
    "total": 2,
    "leves": 1,
    "moderadas": 1,
    "graves": 0,
    "resueltas": 1,
    "pendientes": 1
  }
  ```
