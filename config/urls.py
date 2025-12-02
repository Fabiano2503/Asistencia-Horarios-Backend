from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/practicantes/', include('apps.practicantes.infrastructure.urls')),
    path('api/bot/', include('apps.bot_discord.infrastructure.urls')),

    # Rutas de reportes (carpeta apps/reportes)
    path("api/reportes/", include(("apps.reportes.infrastructure.urls", "reportes"), namespace="reportes")),

]
