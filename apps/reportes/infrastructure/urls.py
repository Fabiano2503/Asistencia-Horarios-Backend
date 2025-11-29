from django.urls import path
from . import views

urlpatterns = [
    path("api/v1/reports/summary", views.dashboard_summary),
    path("api/v1/reports/warnings/current-month", views.advertencias_mes_actual),
    path("api/v1/reports/warnings/history", views.historial_advertencias),
    path("api/v1/reports/hours/compliance-detail", views.detalle_cumplimiento_horas),
    path("api/v1/reports/hours/global-summary", views.resumen_global_horas),
    path("api/v1/reports/permissions/current-week", views.permisos_semana_actual),
    path("api/v1/reports/permissions/by-employee", views.resumen_permisos_practicante),
    path("api/v1/reports/export/weekly", views.export_reporte_semanal),
    path("api/v1/reports/export/monthly", views.export_reporte_mensual),
]
