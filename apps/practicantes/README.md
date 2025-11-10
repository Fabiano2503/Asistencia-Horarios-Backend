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
