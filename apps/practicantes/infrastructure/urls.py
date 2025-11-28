from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

# Importaciones de vistas
from .views import (
    PracticanteViewSet,
    AsistenciaViewSet,
    HorarioViewSet,
    InicioViewSet,
    CalendarioSemanalViewSet,
    EstadisticasPersonalesViewSet,
    AdvertenciaViewSet
)

# Importaciones de vistas de historial
from .api.views.historial_views import (
    HistorialAPIView,
    EstadisticasHistorialAPIView,
    RegistrarAccionAPIView
)

# 1. Router principal para los practicantes (CRUD básico)
router = DefaultRouter()
router.register(r'', PracticanteViewSet, basename='practicante')

# 2. Router para el dashboard
# Usamos SimpleRouter ya que no necesitamos el detalle de las rutas
# que proporciona DefaultRouter
api_router = SimpleRouter()
api_router.register(r'inicio', InicioViewSet, basename='api-inicio')
api_router.register(r'mi-asistencia', AsistenciaViewSet, basename='api-mi-asistencia')
api_router.register(r'mi-horario', HorarioViewSet, basename='api-mi-horario')
api_router.register(r'calendario-semanal', CalendarioSemanalViewSet, basename='api-calendario-semanal')
api_router.register(r'estadisticas-personales', EstadisticasPersonalesViewSet, basename='api-estadisticas-personales')
api_router.register(r'advertencias', AdvertenciaViewSet, basename='api-advertencias')

# 3. URLs para el módulo de historial
# Estas son rutas APIView personalizadas que no usan ViewSets
historial_urlpatterns = [
    path('historial/', HistorialAPIView.as_view(), name='historial-list'),
    path('historial/estadisticas/', EstadisticasHistorialAPIView.as_view(), name='historial-estadisticas'),
    path('historial/acciones/', RegistrarAccionAPIView.as_view(), name='registrar-accion'),
]

# Configuración final de URLs
urlpatterns = [
    # Rutas de la API principal
    path('', include(router.urls)),
    
    # Rutas del dashboard bajo /api/dashboard/
    path('api/dashboard/', include(api_router.urls)),
    
    # Rutas del historial
    path('api/', include(historial_urlpatterns)),
]
