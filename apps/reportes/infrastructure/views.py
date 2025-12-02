from rest_framework.response import Response
from django.http import HttpResponse
import asyncio
from io import BytesIO

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


def run_async(func, *args, **kwargs):
    return asyncio.run(func(*args, **kwargs))


def dashboard_summary(request):
    data = run_async(get_dashboard_summary)
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
    return Response(data)


def resumen_global_horas(request):
    data = run_async(get_resumen_global_horas)
    return Response(data)


def permisos_semana_actual(request):
    data = run_async(get_permisos_semana_actual)
    return Response(data)


def resumen_permisos_practicante(request):
    data = run_async(get_resumen_permisos_practicante)
    return Response(data)


def export_reporte_semanal(request):
    buffer = BytesIO()
    run_async(generar_reporte_semanal_excel, buffer)
    buffer.seek(0)

    response = HttpResponse(
        buffer.read(),
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = 'attachment; filename="Reporte_Semanal.xlsx"'
    return response


def export_reporte_mensual(request):
    buffer = BytesIO()
    run_async(generar_reporte_mensual_excel, buffer)
    buffer.seek(0)

    response = HttpResponse(
        buffer.read(),
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = 'attachment; filename="Reporte_Mensual.xlsx"'
    return response
