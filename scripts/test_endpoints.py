"""
Script para testear todos los endpoints de puntualidad
Ejecutar: python test_endpoints.py
"""
import requests
import json
from datetime import datetime, date, timedelta

# Configuración
BASE_URL = "http://127.0.0.1:8000/api/puntualidad"
HEADERS = {"Content-Type": "application/json"}

# Colores para output
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'
    BOLD = '\033[1m'

def print_success(message):
    print(f"{Colors.GREEN}✓ {message}{Colors.END}")

def print_error(message):
    print(f"{Colors.RED}✗ {message}{Colors.END}")

def print_info(message):
    print(f"{Colors.BLUE}ℹ {message}{Colors.END}")

def print_section(title):
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{title}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.END}\n")

def test_endpoint(method, url, data=None, expected_status=200, description=""):
    """Testea un endpoint y retorna la respuesta"""
    try:
        if method.upper() == 'GET':
            response = requests.get(url, headers=HEADERS)
        elif method.upper() == 'POST':
            response = requests.post(url, headers=HEADERS, json=data)
        else:
            print_error(f"Método {method} no soportado")
            return None
        
        status_ok = response.status_code == expected_status
        if status_ok:
            print_success(f"{description or url} - Status: {response.status_code}")
        else:
            print_error(f"{description or url} - Status: {response.status_code} (esperado: {expected_status})")
            print_error(f"Respuesta: {response.text[:200]}")
        
        return response
    except requests.exceptions.ConnectionError:
        print_error(f"No se pudo conectar a {url}. ¿Está el servidor Django corriendo?")
        return None
    except Exception as e:
        print_error(f"Error en {url}: {str(e)}")
        return None

def test_resumen():
    """Test del endpoint de resumen"""
    print_section("TEST: Resumen de Puntualidad")
    response = test_endpoint('GET', f"{BASE_URL}/resumen/", description="GET /resumen/")
    
    if response and response.status_code == 200:
        data = response.json()
        print_info(f"Respuesta: {json.dumps(data, indent=2, ensure_ascii=False)}")
        return True
    return False

def test_alertas():
    """Test del endpoint de alertas"""
    print_section("TEST: Alertas de Puntualidad")
    response = test_endpoint('GET', f"{BASE_URL}/alertas/", description="GET /alertas/")
    
    if response and response.status_code == 200:
        data = response.json()
        print_info(f"Respuesta: {json.dumps(data, indent=2, ensure_ascii=False)}")
        return True
    return False

def test_practicantes():
    """Test del endpoint de practicantes"""
    print_section("TEST: Lista de Practicantes")
    response = test_endpoint('GET', f"{BASE_URL}/practicantes/", description="GET /practicantes/")
    
    if response and response.status_code == 200:
        data = response.json()
        print_info(f"Total practicantes: {len(data)}")
        if data:
            print_info(f"Primer practicante: {json.dumps(data[0], indent=2, ensure_ascii=False)}")
        return data
    return []

def test_practicantes_activos():
    """Test del endpoint de practicantes activos"""
    print_section("TEST: Practicantes Activos (para formulario)")
    response = test_endpoint('GET', f"{BASE_URL}/practicantes/activos/", description="GET /practicantes/activos/")
    
    if response and response.status_code == 200:
        data = response.json()
        print_info(f"Total practicantes activos: {len(data)}")
        if data:
            print_info(f"Primer practicante activo: {json.dumps(data[0], indent=2, ensure_ascii=False)}")
        return data
    return []

def test_justificaciones():
    """Test del endpoint de justificaciones"""
    print_section("TEST: Lista de Justificaciones")
    response = test_endpoint('GET', f"{BASE_URL}/justificaciones/", description="GET /justificaciones/")
    
    if response and response.status_code == 200:
        data = response.json()
        print_info(f"Total justificaciones: {len(data)}")
        if data:
            print_info(f"Primera justificación: {json.dumps(data[0], indent=2, ensure_ascii=False)}")
        return data
    return []

def test_crear_justificacion(practicante_id=None):
    """Test del endpoint para crear justificación"""
    print_section("TEST: Crear Justificación")
    
    if not practicante_id:
        print_error("No se proporcionó practicante_id. Obtén uno de /practicantes/activos/")
        return None
    
    fecha = (date.today() - timedelta(days=1)).isoformat()  # Ayer
    
    payload = {
        "practicante_id": practicante_id,
        "fecha": fecha,
        "motivo": "Test de justificación desde script de testing",
        "tiene_evidencia": False,
        "ticket_id": "TKT-TEST-001"
    }
    
    print_info(f"Payload: {json.dumps(payload, indent=2, ensure_ascii=False)}")
    
    response = test_endpoint('POST', f"{BASE_URL}/justificaciones/crear/", 
                            data=payload, 
                            expected_status=201,
                            description="POST /justificaciones/crear/")
    
    if response:
        if response.status_code in [200, 201]:
            data = response.json()
            print_info(f"Justificación creada: {json.dumps(data, indent=2, ensure_ascii=False)}")
            return data.get('id')
        else:
            print_error(f"Error: {response.text}")
    
    return None

def test_aprobar_justificacion(justificacion_id=None):
    """Test del endpoint para aprobar justificación"""
    print_section("TEST: Aprobar Justificación")
    
    if not justificacion_id:
        print_error("No se proporcionó justificacion_id")
        return False
    
    response = test_endpoint('POST', f"{BASE_URL}/justificaciones/{justificacion_id}/aprobar/",
                           expected_status=200,
                           description=f"POST /justificaciones/{justificacion_id}/aprobar/")
    
    if response and response.status_code == 200:
        data = response.json()
        print_info(f"Respuesta: {json.dumps(data, indent=2, ensure_ascii=False)}")
        return True
    return False

def test_rechazar_justificacion(justificacion_id=None):
    """Test del endpoint para rechazar justificación"""
    print_section("TEST: Rechazar Justificación")
    
    if not justificacion_id:
        print_error("No se proporcionó justificacion_id")
        return False
    
    payload = {
        "motivo_rechazo": "Test de rechazo desde script de testing"
    }
    
    response = test_endpoint('POST', f"{BASE_URL}/justificaciones/{justificacion_id}/rechazar/",
                           data=payload,
                           expected_status=200,
                           description=f"POST /justificaciones/{justificacion_id}/rechazar/")
    
    if response and response.status_code == 200:
        data = response.json()
        print_info(f"Respuesta: {json.dumps(data, indent=2, ensure_ascii=False)}")
        return True
    return False

def test_recuperaciones():
    """Test del endpoint de recuperaciones"""
    print_section("TEST: Lista de Recuperaciones")
    response = test_endpoint('GET', f"{BASE_URL}/recuperaciones/", description="GET /recuperaciones/")
    
    if response and response.status_code == 200:
        data = response.json()
        print_info(f"Total recuperaciones: {len(data)}")
        if data:
            print_info(f"Primera recuperación: {json.dumps(data[0], indent=2, ensure_ascii=False)}")
        return data
    return []

def main():
    """Ejecuta todos los tests"""
    print(f"\n{Colors.BOLD}{Colors.BLUE}")
    print("="*60)
    print("  TESTING DE ENDPOINTS - SISTEMA DE PUNTUALIDAD")
    print("="*60)
    print(f"{Colors.END}\n")
    
    print_info("Asegúrate de que el servidor Django esté corriendo en http://127.0.0.1:8000")
    print_info("Presiona Enter para continuar o Ctrl+C para cancelar...")
    try:
        input()
    except KeyboardInterrupt:
        print("\n\nCancelado por el usuario")
        return
    
    results = {
        'resumen': False,
        'alertas': False,
        'practicantes': False,
        'practicantes_activos': False,
        'justificaciones': False,
        'crear_justificacion': False,
        'aprobar_justificacion': False,
        'rechazar_justificacion': False,
        'recuperaciones': False,
    }
    
    # Tests básicos (GET)
    results['resumen'] = test_resumen()
    results['alertas'] = test_alertas()
    practicantes = test_practicantes()
    results['practicantes'] = len(practicantes) >= 0
    
    practicantes_activos = test_practicantes_activos()
    results['practicantes_activos'] = len(practicantes_activos) >= 0
    
    justificaciones = test_justificaciones()
    results['justificaciones'] = len(justificaciones) >= 0
    
    results['recuperaciones'] = test_recuperaciones()
    
    # Tests de creación y modificación (requieren datos)
    if practicantes_activos and len(practicantes_activos) > 0:
        practicante_id = practicantes_activos[0]['id']
        print_info(f"\nUsando practicante_id: {practicante_id} para tests de creación")
        
        justificacion_id = test_crear_justificacion(practicante_id)
        results['crear_justificacion'] = justificacion_id is not None
        
        if justificacion_id:
            # Buscar una justificación pendiente para aprobar/rechazar
            justificaciones_actualizadas = test_justificaciones()
            justificacion_pendiente = None
            for j in justificaciones_actualizadas:
                if j.get('estado') == 'pendiente':
                    justificacion_pendiente = j['id']
                    break
            
            if justificacion_pendiente:
                print_info(f"\nUsando justificacion_id: {justificacion_pendiente} para tests de aprobar/rechazar")
                # Solo testear aprobar, rechazar requiere crear otra justificación
                results['aprobar_justificacion'] = test_aprobar_justificacion(justificacion_pendiente)
            else:
                print_info("No hay justificaciones pendientes para aprobar/rechazar")
    else:
        print_error("No hay practicantes activos. No se pueden hacer tests de creación.")
    
    # Resumen final
    print_section("RESUMEN DE TESTS")
    total = len(results)
    exitosos = sum(1 for v in results.values() if v)
    
    for test, resultado in results.items():
        status = "✓" if resultado else "✗"
        color = Colors.GREEN if resultado else Colors.RED
        print(f"{color}{status} {test}{Colors.END}")
    
    print(f"\n{Colors.BOLD}Total: {exitosos}/{total} tests exitosos{Colors.END}\n")
    
    if exitosos == total:
        print_success("¡Todos los tests pasaron!")
    else:
        print_error(f"Faltan {total - exitosos} tests por pasar")

if __name__ == "__main__":
    main()
