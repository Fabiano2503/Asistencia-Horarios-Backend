# apps/reportes/infrastructure/views.py

from rest_framework.response import Response
from django.http import HttpResponse
import asyncio
from io import BytesIO

from apps.reportes.application.services import (
    obtener_resumen_dashboard,
    obtener_advertencias_mes_actual,
    obtener_advertencias_historico,
    obtener_permisos_semana_actual,
    obtener_permisos_por_practicante,
    obtener_resumen_global_horas,
    obtener_detalle_cumplimiento_horas,
    generar_reporte_semanal_excel,
    generar_reporte_mensual_excel,
)

# -----------------------------
# Helper para ejecutar funciones async
# -----------------------------
def run_async(func, *args, **kwargs):
    return asyncio.run(func(*args, **kwargs))


# -----------------------------
# ENDPOINTS DE API
# -----------------------------

def dashboard_summary(request):
    data = obtener_resumen_dashboard()
    return Response(data)


def advertencias_mes_actual(request):
    data = obtener_advertencias_mes_actual()
    return Response(data)


def advertencias_historico(request):
    data = obtener_advertencias_historico()
    return Response(data)


def permisos_semana_actual(request):
    data = obtener_permisos_semana_actual()
    return Response(data)


def permisos_por_practicante(request):
    data = obtener_permisos_por_practicante()
    return Response(data)


def resumen_global_horas(request):
    data = obtener_resumen_global_horas()
    return Response(data)


def detalle_cumplimiento_horas(request):
    data = obtener_detalle_cumplimiento_horas()
    return Response(data)


# -----------------------------
# EXPORTACIONES EXCEL
# -----------------------------

def export_reporte_semanal(request):
    buffer = BytesIO()
    run_async(generar_reporte_semanal_excel, buffer)

    buffer.seek(0)
    response = HttpResponse(
        buffer.read(),
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
    response["Content-Disposition"] = 'attachment; filename="reporte_semanal.xlsx"'
    return response


def export_reporte_mensual(request):
    buffer = BytesIO()
    run_async(generar_reporte_mensual_excel, buffer)

    buffer.seek(0)
    response = HttpResponse(
        buffer.read(),
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
    response["Content-Disposition"] = 'attachment; filename="reporte_mensual.xlsx"'
    return response
