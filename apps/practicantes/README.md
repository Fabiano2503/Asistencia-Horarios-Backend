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

## Reforzamiento

### Listar y Filtrar Reforzamientos

- **GET /api/reforzamiento/**
- **Query Params:**
  - `practicante` (integer): Filtra por ID del practicante.
  - `fecha_inicio` (date): Filtra por fecha de inicio.
  - `fecha_fin` (date): Filtra por fecha de fin.
  - `estado` (string): Filtra por estado (`pendiente`, `en_progreso`, `completado`).
- **Respuesta:**
  ```json
  {
    "count": 50,
    "next": "https://IP:PUERTO/api/reforzamiento/?page=2",
    "previous": null,
    "results": [
      {
        "id": 1,
        "practicante": 1,
        "fecha_inicio": "2025-01-15",
        "fecha_fin": "2025-02-15",
        "descripcion": "Reforzamiento en Python",
        "estado": "en_progreso"
      },
      {
        "id": 2,
        "practicante": 5,
        "fecha_inicio": "2025-01-10",
        "fecha_fin": "2025-02-10",
        "descripcion": "Reforzamiento en Django",
        "estado": "pendiente"
      }
    ]
  }
  ```

### Obtener Detalle de un Reforzamiento

- **GET /api/reforzamiento/{id}/**

### Crear un Reforzamiento

- **POST /api/reforzamiento/**
- **Body:**
  ```json
  {
    "practicante": 1,
    "fecha_inicio": "2025-01-15",
    "fecha_fin": "2025-02-15",
    "descripcion": "Reforzamiento en Python",
    "estado": "pendiente"
  }
  ```

### Actualizar un Reforzamiento

- **PUT /api/reforzamiento/{id}/**
- **PATCH /api/reforzamiento/{id}/**
- **Body:** (similar al de creación)

### Eliminar un Reforzamiento

- **DELETE /api/reforzamiento/{id}/**

### Actualizar Área y Motivo de Reforzamiento

- **PATCH /api/reforzamiento/{id}/actualizar_info/**
- **Body:**
  ```json
  {
    "area": "Backend",
    "motivo": "Dificultades con Django ORM"
  }
  ```

### Completar Reforzamiento

- **POST /api/reforzamiento/{id}/completar/**
- **Respuesta:**
  ```json
  {
    "id": 1,
    "practicante": 1,
    "fecha_inicio": "2025-01-15",
    "fecha_fin": "2025-02-15",
    "descripcion": "Reforzamiento en Python",
    "estado": "completado"
  }
  ```

### Reintegrar Practicante

- **POST /api/reforzamiento/{id}/reintegrar/**
- **Respuesta:**
  ```json
  {
    "id": 1,
    "practicante": 1,
    "fecha_inicio": "2025-01-15",
    "fecha_fin": "2025-02-15",
    "descripcion": "Reforzamiento en Python",
    "estado": "reintegrado"
  }
  ```

### Obtener Métricas de Reforzamiento

- **GET /api/reforzamiento/metricas/**
- **Respuesta:**
  ```json
  {
    "en_reforzamiento": 0,
    "completados": 0,
    "reintegrados": 0,
    "total": 0
  }
  ```
