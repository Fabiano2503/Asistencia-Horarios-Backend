from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PracticanteViewSet, ReforzamientoViewSet  

router = DefaultRouter()
router.register(r'practicantes', PracticanteViewSet, basename='practicante')
router.register(r'reforzamiento', ReforzamientoViewSet, basename='reforzamiento')

urlpatterns = [
    path('', include(router.urls)),
]
