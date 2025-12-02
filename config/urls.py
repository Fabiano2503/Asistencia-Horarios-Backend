from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/practicantes/', include('apps.practicantes.infrastructure.urls')),
    path('api/bot/', include('apps.bot_discord.infrastructure.urls')),

    # Rutas de reportes (carpeta apps/reportes)
    path('api/v1/reports/', include('apps.reportes.infrastructure.urls')),

    path('api/puntualidad/', include('apps.puntualidad.urls')),
]
