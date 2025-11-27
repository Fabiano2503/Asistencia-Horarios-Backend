# Módulo de Monitoreo del Bot de Discord

Este módulo se encarga de monitorear y gestionar el estado de un bot de Discord en tiempo real, utilizando Django Rest Framework y Django Channels.

## Arquitectura Hexagonal

El módulo sigue una arquitectura hexagonal (Ports & Adapters) para separar las preocupaciones:

-   **Dominio**: Contiene la lógica de negocio pura y las entidades (`entities.py`, `repositories.py`).
-   **Aplicación**: Orquesta los flujos de trabajo y casos de uso (`services.py`).
-   **Infraestructura**: Implementa los detalles técnicos como la base de datos, API REST y WebSockets (`models.py`, `views.py`, `consumers.py`, etc.).

## Endpoints REST

### Recibir Métricas

-   **Endpoint**: `POST /api/bot/metrics/`
-   **Autenticación**: `Authorization: Bearer <BOT_API_KEY>`
-   **Payload**:
    ```json
    {
      "resumen": {
        "servidores_conectados": 5,
        "eventos_procesados_hoy": 1230,
        "uptime_porcentaje": 99.8,
        "ultima_sincronizacion": "2025-11-13T18:00:00.831984Z"
      },
      "estado": {
        "status": "online",
        "uptime_dias": 15,
        "latencia_ms": 45,
        "ultima_conexion": "2025-11-13T17:58:00.831984Z"
      },
      "servers": [
        {
          "server_id": 987654321,
          "server_name": "RPSOFT",
          "miembros": 87,
          "canales": 12,
          "status": "conectado"
        }
      ]
    }
    ```

### Obtener Métricas

-   `GET /api/bot/resumen/`: Retorna las métricas globales más recientes.
-   `GET /api/bot/estado/`: Retorna el estado operativo actual del bot.
-   `GET /api/bot/servers/`: Lista los servidores con sus métricas actuales.

## WebSocket

-   **Ruta**: `ws://IP:PUERTO/ws/bot/metrics/`
-   **Funcionalidad**:
    -   Al conectarse, el cliente se une a un grupo que recibe actualizaciones de métricas.
    -   Cada vez que el bot envía nuevas métricas a través del endpoint POST, se emite un mensaje a todos los clientes conectados.
-   **Mensaje Emitido**: El mismo formato que el payload de `POST /api/bot/metrics/`.
