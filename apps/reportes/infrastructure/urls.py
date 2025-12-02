from django.urls import path
from . import views


app_name = "practicantes"

urlpatterns = [
    path("summary", views.dashboard_summary, name="summary"),

    path("warnings/current-month", views.advertencias_mes_actual, name="warnings-current"),
    path("warnings/history", views.historial_advertencias, name="warnings-history"),

    path("hours/compliance-detail", views.detalle_cumplimiento_horas, name="compliance-detail"),
    path("hours/global-summary", views.resumen_global_horas, name="global-summary"),

    path("permissions/current-week", views.permisos_semana_actual, name="permissions-week"),
    path("permissions/by-employee", views.resumen_permisos_practicante, name="permissions-employee"),

    path("export/weekly", views.export_reporte_semanal, name="export-weekly"),
    path("export/monthly", views.export_reporte_mensual, name="export-monthly"),
]
