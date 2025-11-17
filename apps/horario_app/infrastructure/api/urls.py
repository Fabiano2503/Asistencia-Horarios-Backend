from django.urls import path
from .views import HorarioAPI, PracticantesAPI, PendientesAPI

urlpatterns = [
    path('horarios/', HorarioAPI.as_view(), name='horarios'),
    path('practicantes/', PracticantesAPI.as_view(), name='practicantes'),
    path('pendientes/', PendientesAPI.as_view(), name='pendientes'),
]