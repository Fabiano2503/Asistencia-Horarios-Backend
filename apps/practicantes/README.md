# Módulo de Practicantes

Este módulo gestiona la información de los practicantes y su historial de acciones.

## Módulo de Historial de Practicantes

Este módulo permite gestionar el historial de acciones realizadas por y sobre los practicantes, incluyendo advertencias, traslados y expulsiones.

### Modelo de Datos

#### Acción de Practicante
```typescript
{
  "id": number,
  "fecha": "ISO8601 datetime",
  "practicante_id": number,
  "tipo_accion": "advertencia" | "traslado" | "expulsion" | "otro",
  "descripcion": string,
  "usuario": string,
  "detalles": object
}
```

#### Estadísticas de Historial
```typescript
{
  "total_registros": number,
  "total_advertencias": number,
  "total_traslados": number,
  "total_expulsiones": number,
  "total_practicantes": number,
  "total_activos": number,
  "total_trasladados": number,
  "total_expulsados": number,
  "total_en_reforzamiento": number
}
```

## Endpoints

## Endpoints de Historial

### Obtener Historial de Acciones

- **GET /api/practicantes/historial/**
- **Query Params:**
  - `busqueda` (string): Texto para buscar en descripción o detalles
  - `area` (string): Filtrar por área del practicante
  - `tipo_accion` (string): Tipo de acción (advertencia, traslado, expulsion, otro)
  - `estado` (string): Estado final del practicante (activo, en_recuperacion, en_riesgo, trasladado, expulsado)
  - `fecha_desde` (date): Fecha de inicio (YYYY-MM-DD)
  - `fecha_hasta` (date): Fecha de fin (YYYY-MM-DD)
  - `pagina` (int): Número de página (default: 1)
  - `por_pagina` (int): Elementos por página (default: 10)
- **Respuesta Exitosa (200):**
  ```json
  {
    "data": [
      {
        "id": 1,
        "fecha": "2023-01-01T12:00:00Z",
        "practicante_id": 1,
        "tipo_accion": "advertencia",
        "descripcion": "Llegada tarde",
        "usuario": "admin",
        "detalles": {"motivo": "Retraso injustificado"}
      }
    ],
    "paginacion": {
      "total": 1,
      "pagina": 1,
      "por_pagina": 10,
      "total_paginas": 1
    }
  }
  ```

### Obtener Estadísticas del Historial

- **GET /api/practicantes/historial/estadisticas/**
- **Respuesta Exitosa (200):**
  ```json
  {
    "total_registros": 100,
    "total_advertencias": 50,
    "total_traslados": 20,
    "total_expulsiones": 5,
    "total_practicantes": 30,
    "total_activos": 25,
    "total_trasladados": 3,
    "total_expulsados": 2,
    "total_en_reforzamiento": 5
  }
  ```

### Registrar Nueva Acción

- **POST /api/practicantes/historial/acciones/**
- **Body:**
  ```json
  {
    "practicante_id": 1,
    "tipo_accion": "advertencia",
    "descripcion": "Llegada tarde",
    "detalles": {
      "motivo": "Retraso injustificado",
      "gravedad": "media"
    }
  }
  ```
- **Respuesta Exitosa (201):**
  ```json
  {
    "id": 1,
    "fecha": "2023-01-01T12:00:00Z",
    "practicante_id": 1,
    "tipo_accion": "advertencia",
    "descripcion": "Llegada tarde",
    "usuario": "admin",
    "detalles": {"motivo": "Retraso injustificado"}
  }
  ```
- **Códigos de Error:**
  - 400: Datos de entrada inválidos o faltantes
  - 500: Error interno del servidor

## Endpoints de Gestión de Practicantes

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
