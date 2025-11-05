# Módulo de Practicantes

Este módulo gestiona la información de los practicantes.

## Endpoints

### Listar y Filtrar Practicantes

- **GET /api/practicantes/**
- **Query Params:**
  - `nombre` (string): Filtra por nombre.
  - `correo` (string): Filtra por correo electrónico.
  - `estado` (string): Filtra por estado (`activo`, `en_recuperacion`, `en_riesgo`).

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
    "semestre": 0,
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
