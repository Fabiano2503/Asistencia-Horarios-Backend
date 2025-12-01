# Módulo de Monitoreo del Bot de Discord

Este módulo se encarga de monitorear y gestionar el estado de un bot de Discord en tiempo real, utilizando Django Rest Framework y Django Channels.

## Arquitectura Hexagonal

El módulo sigue una arquitectura hexagonal (Ports & Adapters) para separar las preocupaciones:

- **Domain**: Contiene la lógica de negocio pura y las entidades
- **Application**: Orquesta los flujos de trabajo y casos de uso
- **Infrastructure**: Implementa los detalles técnicos (base de datos, API REST, WebSockets)

## Endpoints REST

### Enviar Métricas del Bot

- **Endpoint**: `POST /api/bot/metricas/`
- **Autenticación**: `Authorization: Bearer <BOT_API_KEY>`
- **Headers requeridos**:
  - `Authorization: Bearer your_secret_key_here`
  - `Content-Type: application/json`
- **Payload**:
```json
{
  "resumen": {
    "servidores_conectados": 5,
    "eventos_procesados_hoy": 150,
    "uptime_porcentaje": 98.5,
    "ultima_sincronizacion": "2025-11-27T10:30:00Z"
  },
  "estado": {
    "status": "online",
    "uptime_dias": 7,
    "latencia_ms": 45,
    "ultima_conexion": "2025-11-27T10:30:00Z"
  },
  "servers": [
    {
      "server_id": "123456789012345678",
      "server_name": "Servidor Principal",
      "miembros": 150,
      "canales": 25,
      "status": "online",
      "ultima_actualizacion": "2025-11-27T10:30:00Z"
    }
  ]
}
```

### Consultar Estado del Bot

- `GET /api/bot/resumen/` - Retorna las métricas globales más recientes
- `GET /api/bot/estado/` - Retorna el estado operativo actual del bot
- `GET /api/bot/servidores/` - Lista los servidores con sus métricas actuales

### Gestionar Estado del Bot

- **Endpoint**: `POST /api/bot/estado/`
- **Autenticación**: `Authorization: Bearer <BOT_API_KEY>`
- **Payload**:
```json
{
  "status": "maintenance"
}
```

## WebSocket

- **Ruta**: `ws://IP:PUERTO/ws/bot/metrics/`
- **Funcionalidad**:
  - Al conectarse, el cliente se une al grupo 'metricas_bot'
  - Cada vez que el bot envía métricas, se emite actualización a todos los clientes conectados
- **Mensaje Emitido**: Formato completo del payload de métricas

## Respuestas de API

### Respuesta Exitosa (Métricas)
```json
{
  "message": "Métricas recibidas y emitidas"
}
```

### Respuesta de Resumen
```json
{
  "servidores_conectados": 5,
  "eventos_procesados_hoy": 150,
  "uptime_porcentaje": 98.5,
  "ultima_sincronizacion": "2025-11-27T10:30:00"
}
```

### Respuesta de Estado
```json
{
  "status": "online",
  "uptime_dias": 7,
  "latencia_ms": 45,
  "ultima_conexion": "2025-11-27T10:30:00"
}
```

### Respuesta de Servidores
```json
[
  {
    "server_id": "123456789012345678",
    "server_name": "Servidor Principal",
    "miembros": 150,
    "canales": 25,
    "status": "online",
    "ultima_actualizacion": "2025-11-27T10:30:00"
  }
]
```

## Seguridad

- **API Key requerida** para envío de métricas y cambios de estado
- **Solo administradores** pueden acceder a métricas del bot
- **Validación de payload** en todos los endpoints
