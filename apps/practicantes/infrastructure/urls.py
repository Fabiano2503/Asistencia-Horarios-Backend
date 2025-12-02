from django.urls import path
from . import views

app_name = "practicantes"

urlpatterns = [
    # Estas líneas ahora encuentran las funciones definidas en views.py
    path("advertencias/mes/", views.advertencias_mes_actual, name="warnings-current"),
    path("advertencias/historico/", views.advertencias_historico, name="warnings-history"),
    path("permisos/semana/", views.permisos_semana_actual, name="permissions-week"),
    path("permisos/practicante/", views.permisos_por_practicante, name="permissions-employee"),
    path("exportar/semanal/", views.export_reporte_semanal, name="export-weekly"),
    path("exportar/mensual/", views.export_reporte_mensual, name="export-monthly"),
]
