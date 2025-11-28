from django.urls import path, include
# Configuración de URLs para el módulo de practicantes
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import (
    PracticanteViewSet, 
    AsistenciaViewSet, 
    HorarioViewSet, 
    InicioViewSet, 
    CalendarioSemanalViewSet, 
    EstadisticasPersonalesViewSet, 
    AdvertenciaViewSet
)
from .api.views.historial_views import (
    HistorialAPIView,
    EstadisticasHistorialAPIView,
    RegistrarAccionAPIView
)

# Router para los practicantes
router = DefaultRouter()
router.register(r'', PracticanteViewSet, basename='practicante')

# Router para el dashboard
dashboard_router = SimpleRouter()
dashboard_router.register(r"inicio", InicioViewSet, basename="dashboard-inicio")
dashboard_router.register(r"mi-asistencia", AsistenciaViewSet, basename="dashboard-asistencia")
dashboard_router.register(r"mi-horario", HorarioViewSet, basename="dashboard-horario")
dashboard_router.register(r"calendario-semanal", CalendarioSemanalViewSet, basename="dashboard-calendario")
dashboard_router.register(r"estadisticas-personales", EstadisticasPersonalesViewSet, basename="dashboard-estadisticas")
dashboard_router.register(r"advertencias", AdvertenciaViewSet, basename="dashboard-advertencias")

# URLs para el historial de practicantes
historial_urlpatterns = [
    path('historial/', HistorialAPIView.as_view(), name='historial-list'),
    path('historial/estadisticas/', EstadisticasHistorialAPIView.as_view(), name='historial-estadisticas'),
    path('historial/acciones/', RegistrarAccionAPIView.as_view(), name='registrar-accion'),
]

# Configuración final de URLs
urlpatterns = [
    path('', include(router.urls)),
    path('dashboard/', include(dashboard_router.urls)),
    path('', include(historial_urlpatterns)),
]
