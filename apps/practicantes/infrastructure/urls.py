from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

# Importaciones de vistas del dashboard
from .views import (
    AsistenciaViewSet,
    HorarioViewSet,
    InicioViewSet,
    CalendarioSemanalViewSet,
    EstadisticasPersonalesViewSet,
    AdvertenciaViewSet,
    PracticanteViewSet
)

# Importaciones de vistas de historial
from .api.views.historial_views import (
    HistorialAPIView,
    EstadisticasHistorialAPIView,
    RegistrarAccionAPIView
)

# 1. Router principal para los practicantes (CRUD básico)
router = DefaultRouter()
router.register(r'practicantes', PracticanteViewSet, basename='practicante')

# 2. Router para el dashboard
dashboard_router = SimpleRouter()
dashboard_router.register(r'inicio', InicioViewSet, basename='dashboard-inicio')
dashboard_router.register(r'mi-asistencia', AsistenciaViewSet, basename='dashboard-asistencia')
dashboard_router.register(r'mi-horario', HorarioViewSet, basename='dashboard-horario')
dashboard_router.register(r'calendario-semanal', CalendarioSemanalViewSet, basename='dashboard-calendario')
dashboard_router.register(r'estadisticas-personales', EstadisticasPersonalesViewSet, basename='dashboard-estadisticas')
dashboard_router.register(r'advertencias', AdvertenciaViewSet, basename='dashboard-advertencias')

# 3. URLs para el módulo de historial
historial_urlpatterns = [
    path('historial/', HistorialAPIView.as_view(), name='historial-list'),
    path('historial/estadisticas/', EstadisticasHistorialAPIView.as_view(), name='historial-estadisticas'),
    path('historial/acciones/', RegistrarAccionAPIView.as_view(), name='registrar-accion'),
]

# Configuración final de URLs
urlpatterns = [
    # API v1 - Todas las rutas bajo /api/v1/
    path('api/v1/', include([
        # Rutas de la API principal
        path('', include(router.urls)),
        
        # Rutas del dashboard
        path('dashboard/', include(dashboard_router.urls)),
        
        # Rutas del historial
        path('', include(historial_urlpatterns)),
    ])),
]
