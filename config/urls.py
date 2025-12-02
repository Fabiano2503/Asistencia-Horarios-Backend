from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Apps existentes
    path('api/practicantes/', include('apps.practicantes.infrastructure.urls')),
    path('api/bot/', include('apps.bot_discord.infrastructure.urls')),

    # Nueva app puntualidad
    path('api/puntualidad/', include('apps.puntualidad.urls')),

    # Nueva app reportes
    path('api/v1/reports/', include('apps.reporte.infrastructure.urls', namespace='reporte')),
]
