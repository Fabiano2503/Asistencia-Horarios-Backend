"""
Vistas generales del proyecto
"""
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def api_root(request):
    """
    Vista raíz que devuelve información básica de la API en JSON
    """
    return JsonResponse({
        "status": "ok",
        "api": "Sistema de Asistencia y Horarios",
        "version": "1.0.0"
    })

