from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime

from apps.practicantes.application.historial_service import HistorialService
from apps.practicantes.infrastructure.historial_repository import DjangoORMHistorialRepository
from apps.practicantes.domain.historial import (
    TipoAccion,
    EstadoPracticante
)

class HistorialAPIView(APIView):
    def get(self, request):
        # Obtener parámetros de consulta
        busqueda = request.query_params.get('busqueda')
        area = request.query_params.get('area')
        tipo_accion = request.query_params.get('tipo_accion')
        estado = request.query_params.get('estado')
        fecha_desde = request.query_params.get('fecha_desde')
        fecha_hasta = request.query_params.get('fecha_hasta')
        pagina = int(request.query_params.get('pagina', 1))
        por_pagina = int(request.query_params.get('por_pagina', 10))

        try:
            # Inicializar servicio
            service = HistorialService(DjangoORMHistorialRepository())
            
            # Convertir fechas
            fecha_desde_dt = datetime.strptime(fecha_desde, '%Y-%m-%d') if fecha_desde else None
            fecha_hasta_dt = datetime.strptime(fecha_hasta, '%Y-%m-%d') if fecha_hasta else None

            # Obtener historial
            historial, total = service.obtener_historial(
                busqueda=busqueda,
                area=area,
                tipo_accion=TipoAccion(tipo_accion) if tipo_accion else None,
                estado_final=EstadoPracticante(estado) if estado else None,
                fecha_desde=fecha_desde_dt,
                fecha_hasta=fecha_hasta_dt,
                pagina=pagina,
                por_pagina=por_pagina
            )

            return Response({
                'data': [item.__dict__ for item in historial],
                'paginacion': {
                    'total': total,
                    'pagina': pagina,
                    'por_pagina': por_pagina,
                    'total_paginas': (total + por_pagina - 1) // por_pagina
                }
            })

        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {'error': 'Error interno del servidor'}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class EstadisticasHistorialAPIView(APIView):
    def get(self, request):
        try:
            service = HistorialService(DjangoORMHistorialRepository())
            estadisticas = service.obtener_estadisticas()
            return Response(estadisticas.__dict__)
        except Exception as e:
            return Response(
                {'error': 'Error al obtener estadísticas'}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class RegistrarAccionAPIView(APIView):
    def post(self, request):
        try:
            service = HistorialService(DjangoORMHistorialRepository())
            
            # Validar campos requeridos
            required_fields = ['practicante_id', 'tipo_accion', 'descripcion']
            for field in required_fields:
                if field not in request.data:
                    return Response(
                        {'error': f'El campo {field} es requerido'},
                        status=status.HTTP_400_BAD_REQUEST
                    )

            # Registrar la acción
            accion = service.registrar_accion(
                practicante_id=request.data['practicante_id'],
                tipo_accion=request.data['tipo_accion'],
                descripcion=request.data['descripcion'],
                usuario=request.user.username if hasattr(request, 'user') else 'sistema',
                detalles=request.data.get('detalles', {})
            )

            return Response(accion.__dict__, status=status.HTTP_201_CREATED)

        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {'error': 'Error al registrar la acción'}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
