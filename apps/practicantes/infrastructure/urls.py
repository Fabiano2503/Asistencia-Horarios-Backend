from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PracticanteViewSet
from .api.views.historial_views import (
    HistorialAPIView,
    EstadisticasHistorialAPIView,
    RegistrarAccionAPIView
)

router = DefaultRouter()
router.register(r'', PracticanteViewSet, basename='practicante')

# URLs para el historial de practicantes
historial_urlpatterns = [
    path('historial/', HistorialAPIView.as_view(), name='historial-list'),
    path('historial/estadisticas/', EstadisticasHistorialAPIView.as_view(), name='historial-estadisticas'),
    path('historial/acciones/', RegistrarAccionAPIView.as_view(), name='registrar-accion'),
]

urlpatterns = [
    path('', include(router.urls)),
    path('', include(historial_urlpatterns)),
]
