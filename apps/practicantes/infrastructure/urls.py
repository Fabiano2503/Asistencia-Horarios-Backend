from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import PracticanteViewSet, AsistenciaViewSet, HorarioViewSet, InicioViewSet, CalendarioSemanalViewSet, EstadisticasPersonalesViewSet, AdvertenciaViewSet

router = DefaultRouter()
router.register(r'', PracticanteViewSet, basename='practicante')

dashboard_router = SimpleRouter()
dashboard_router.register(r"inicio", InicioViewSet, basename="dashboard-inicio")
dashboard_router.register(r"mi-asistencia", AsistenciaViewSet, basename="dashboard-asistencia")
dashboard_router.register(r"mi-horario", HorarioViewSet, basename="dashboard-horario")
dashboard_router.register(r"calendario-semanal", CalendarioSemanalViewSet, basename="dashboard-calendario")
dashboard_router.register(r"estadisticas-personales", EstadisticasPersonalesViewSet, basename="dashboard-estadisticas")
dashboard_router.register(r"advertencias", AdvertenciaViewSet, basename="dashboard-advertencias")

urlpatterns = [
    path('', include(router.urls)),
    path('dashboard/', include(dashboard_router.urls)),
]
