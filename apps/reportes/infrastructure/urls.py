# apps/reportes/infrastructure/urls.py

from django.urls import path
from . import views

app_name = "reportes"

urlpatterns = [
    path("summary/", views.dashboard_summary, name="summary"),
    path("advertencias/mes/", views.advertencias_mes_actual, name="advertencias_mes_actual"),
   path("advertencias/historico/", views.historial_advertencias, name="advertencias_historico"),
    path("permisos/semana/", views.permisos_semana_actual, name="permisos_semana_actual"),
    path("permisos/practicante/", views.permisos_por_practicante, name="permisos_por_practicante"),
    path("horas/resumen/", views.resumen_global_horas, name="resumen_global_horas"),
    path("horas/detalle/", views.detalle_cumplimiento_horas, name="detalle_cumplimiento_horas"),
    path("export/semanal/", views.export_reporte_semanal, name="export_reporte_semanal"),
    path("export/mensual/", views.export_reporte_mensual, name="export_reporte_mensual"),
]
