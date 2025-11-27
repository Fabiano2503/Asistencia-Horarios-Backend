"""
Script de verificación del backend
Verifica que no haya errores de sintaxis, imports, y que los endpoints estén configurados correctamente
"""
import sys
import os
import django

# Configurar encoding para Windows
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

# Agregar el directorio actual al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

try:
    django.setup()
    print("✓ Django configurado correctamente")
except Exception as e:
    print(f"✗ Error al configurar Django: {e}")
    sys.exit(1)

# Verificar imports
print("\n📦 Verificando imports...")
try:
    from config.views import api_root
    print("✓ config.views importado correctamente")
except Exception as e:
    print(f"✗ Error al importar config.views: {e}")

try:
    from apps.puntualidad.views import (
        resumen_puntualidad,
        alertas_puntualidad,
        practicantes_puntualidad,
        justificaciones,
        recuperaciones,
        crear_justificacion,
        aprobar_justificacion,
        rechazar_justificacion
    )
    print("✓ apps.puntualidad.views importado correctamente")
except Exception as e:
    print(f"✗ Error al importar apps.puntualidad.views: {e}")

try:
    from apps.puntualidad.serializers import JustificacionCreateSerializer
    print("✓ apps.puntualidad.serializers importado correctamente")
except Exception as e:
    print(f"✗ Error al importar apps.puntualidad.serializers: {e}")

# Verificar URLs
print("\n🔗 Verificando URLs...")
try:
    from django.urls import get_resolver
    resolver = get_resolver()
    url_patterns = []
    
    def collect_urls(patterns, prefix=''):
        for pattern in patterns:
            if hasattr(pattern, 'url_patterns'):
                collect_urls(pattern.url_patterns, prefix + str(pattern.pattern))
            else:
                url_patterns.append(prefix + str(pattern.pattern))
    
    collect_urls(resolver.url_patterns)
    
    # Verificar endpoints importantes
    important_urls = [
        '',
        'api/puntualidad/resumen/',
        'api/puntualidad/justificaciones/',
        'api/puntualidad/justificaciones/crear/',
    ]
    
    for url in important_urls:
        if any(url in pattern for pattern in url_patterns):
            print(f"✓ URL '{url}' encontrada")
        else:
            print(f"⚠ URL '{url}' no encontrada")
    
except Exception as e:
    print(f"✗ Error al verificar URLs: {e}")

# Verificar modelos
print("\n🗄️ Verificando modelos...")
try:
    from apps.puntualidad.models import (
        EstadoAsistencia,
        HorarioClases,
        Asistencia,
        AsistenciaRecuperacion
    )
    print("✓ Modelos de puntualidad importados correctamente")
except Exception as e:
    print(f"✗ Error al importar modelos: {e}")

# Verificar que la base de datos esté accesible
print("\n💾 Verificando base de datos...")
try:
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
    print("✓ Conexión a la base de datos OK")
except Exception as e:
    print(f"⚠ Advertencia de base de datos: {e}")

# Verificar settings
print("\n⚙️ Verificando configuración...")
try:
    from django.conf import settings
    
    checks = [
        ('DEBUG', settings.DEBUG),
        ('INSTALLED_APPS', 'apps.puntualidad' in settings.INSTALLED_APPS),
        ('REST_FRAMEWORK', hasattr(settings, 'REST_FRAMEWORK')),
    ]
    
    for check_name, check_result in checks:
        if check_result:
            print(f"✓ {check_name} configurado correctamente")
        else:
            print(f"⚠ {check_name} no configurado o con valor inesperado")
            
except Exception as e:
    print(f"✗ Error al verificar configuración: {e}")

print("\n" + "="*60)
print("✅ Verificación completada")
print("="*60)

