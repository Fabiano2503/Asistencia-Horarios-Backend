#!/usr/bin/env python3
import os
import sys

def main():
    """Punto de entrada del proyecto Django"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'apps.gestion.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "No se pudo importar Django. ¿Está instalado y disponible en tu entorno?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
