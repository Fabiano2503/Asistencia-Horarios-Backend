from rest_framework.response import Response
from . import serializers
from apps.reportes.application.services import (
    get_dashboard_summary,
    get_advertencias_mes_actual,
    get_historial_advertencias,
    get_detalle_cumplimiento_horas,
    get_resumen_global_horas,
    get_permisos_semana_actual,
    get_resumen_permisos_practicante,
    generar_reporte_semanal_excel,
    generar_reporte_mensual_excel,
)

import io
import asyncio


# ----------- HELPERS PARA LLAMAR FUNCIONES ASYNC DESDE DJANGO -----------

def run_async(func, *args, **kwargs):
    """Ejecuta funciones async dentro de Django (sync)."""
    return asyncio.run(func(*args, **kwargs))


# ---------------------- VIEWS ----------------------

def dashboard_summary(request):
    data = run_async(get_dashboard_summary)
    serialized = serializers.dashboard_summary_to_dict(
        type("Obj", (), data)
    )
   return Response(data)


def advertencias_mes_actual(request):
    data = run_async(get_advertencias_mes_actual)
    return Response(data)



def historial_advertencias(request):
    page = int(request.GET.get("page", 1))
    size = int(request.GET.get("size", 20))
    data = run_async(get_historial_advertencias, page, size)
   return Response(data)


def detalle_cumplimiento_horas(request):
    data = run_async(get_detalle_cumplimiento_horas)
    return JsonResponse(data, safe=False)


def resumen_global_horas(request):
    data = run_async(get_resumen_global_horas)
    return Response(data)


def permisos_semana_actual(request):
    data = run_async(get_permisos_semana_actual)
   return Response(data)


def resumen_permisos_practicante(request):
    data = run_async(get_resumen_permisos_practicante)
    return Response(data)



# ---------------------- EXPORTAR EXCEL ----------------------

def export_reporte_semanal(request):
    buffer = io.BytesIO()
    run_async(generar_reporte_semanal_excel, buffer)
    buffer.seek(0)

    return FileResponse(
        buffer,
        as_attachment=True,
        filename="Reporte_Semanal.xlsx",
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )


def export_reporte_mensual(request):
    buffer = io.BytesIO()
    run_async(generar_reporte_mensual_excel, buffer)
    buffer.seek(0)

    return FileResponse(
        buffer,
        as_attachment=True,
        filename="Reporte_Mensual.xlsx",
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
