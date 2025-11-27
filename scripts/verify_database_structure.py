"""
Script para verificar que la estructura de la base de datos
coincida con el ERD proporcionado
Ejecutar: python verify_database_structure.py
"""
import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.db import connection
from django.core.management import execute_from_command_line

def check_table_exists(table_name):
    """Verifica si una tabla existe en la base de datos"""
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT name FROM sqlite_master 
            WHERE type='table' AND name=?
        """, [table_name])
        return cursor.fetchone() is not None

def check_table_structure(table_name, expected_columns):
    """Verifica que una tabla tenga las columnas esperadas"""
    with connection.cursor() as cursor:
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = {row[1]: row[2] for row in cursor.fetchall()}
        
        missing = []
        for col, col_type in expected_columns.items():
            if col not in columns:
                missing.append(f"{col} ({col_type})")
        
        return missing, columns

def main():
    print("\n" + "="*60)
    print("  VERIFICACIÓN DE ESTRUCTURA DE BASE DE DATOS")
    print("  Comparando con el ERD proporcionado")
    print("="*60 + "\n")
    
    # Estructura esperada según el ERD
    expected_structure = {
        'practicante': {
            'id': 'INTEGER',
            'id_discord': 'BIGINT',
            'nombre': 'VARCHAR',
            'apellido': 'VARCHAR',
            'correo': 'VARCHAR',
            'semestre': 'TINYINT',
            'estado': 'VARCHAR'
        },
        'horario_clases': {
            'id': 'INTEGER',
            'practicante_id': 'INTEGER',
            'dia_clase': 'VARCHAR',
            'dia_recuperacion': 'VARCHAR'
        },
        'estado_asistencia': {
            'id': 'INTEGER',
            'estado': 'VARCHAR'
        },
        'asistencia': {
            'id': 'INTEGER',
            'practicante_id': 'INTEGER',
            'fecha': 'DATE',
            'hora_entrada': 'TIME',
            'hora_salida': 'TIME',
            'estado_id': 'INTEGER',
            'motivo': 'VARCHAR'
        },
        'asistencia_recuperacion': {
            'id': 'INTEGER',
            'asistencia_id': 'INTEGER',
            'fecha_recuperacion': 'DATE',
            'hora_entrada': 'TIME',
            'hora_salida': 'TIME',
            'estado': 'VARCHAR'
        }
    }
    
    all_ok = True
    
    for table_name, expected_columns in expected_structure.items():
        print(f"\n📋 Verificando tabla: {table_name}")
        
        if not check_table_exists(table_name):
            print(f"  ❌ La tabla '{table_name}' NO existe")
            print(f"  💡 Ejecuta: python manage.py migrate")
            all_ok = False
            continue
        
        print(f"  ✓ La tabla '{table_name}' existe")
        
        missing, actual_columns = check_table_structure(table_name, expected_columns)
        
        if missing:
            print(f"  ⚠️  Columnas faltantes: {', '.join(missing)}")
            all_ok = False
        else:
            print(f"  ✓ Todas las columnas esperadas están presentes")
        
        # Mostrar columnas actuales
        print(f"  📊 Columnas actuales: {', '.join(actual_columns.keys())}")
    
    # Verificar relaciones (Foreign Keys)
    print("\n" + "="*60)
    print("  VERIFICACIÓN DE RELACIONES (Foreign Keys)")
    print("="*60 + "\n")
    
    relationships = [
        ('horario_clases', 'practicante_id', 'practicante', 'id'),
        ('asistencia', 'practicante_id', 'practicante', 'id'),
        ('asistencia', 'estado_id', 'estado_asistencia', 'id'),
        ('asistencia_recuperacion', 'asistencia_id', 'asistencia', 'id'),
    ]
    
    for table, fk_column, ref_table, ref_column in relationships:
        if check_table_exists(table) and check_table_exists(ref_table):
            print(f"  ✓ {table}.{fk_column} → {ref_table}.{ref_column}")
        else:
            print(f"  ❌ No se puede verificar {table}.{fk_column} (tablas faltantes)")
            all_ok = False
    
    # Resumen final
    print("\n" + "="*60)
    if all_ok:
        print("  ✅ ESTRUCTURA DE BASE DE DATOS CORRECTA")
        print("  Todas las tablas y columnas coinciden con el ERD")
    else:
        print("  ⚠️  ESTRUCTURA INCOMPLETA")
        print("  Ejecuta las migraciones: python manage.py migrate")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()

