from django.urls import path
from . import views

# Nombre del namespace del módulo
app_name = "reporte"

urlpatterns = [
    path("summary", views.dashboard_summary, name="summary"),
    path("warnings/current-month", views.advertencias_mes_actual, name="advertencias_mes"),
    path("warnings/history", views.historial_advertencias, name="advertencias_historial"),

    path("hours/compliance-detail", views.detalle_cumplimiento_horas, name="detalle_cumplimiento"),
    path("hours/global-summary", views.resumen_global_horas, name="resumen_horas"),

    path("permissions/current-week", views.permisos_semana_actual, name="permisos_semana"),
    path("permissions/by-employee", views.resumen_permisos_practicante, name="permisos_empleado"),

    path("export/weekly", views.export_reporte_semanal, name="export_semanal"),
    path("export/monthly", views.export_reporte_mensual, name="export_mensual"),
]
