#!/bin/bash

echo "===================================="
echo "  Iniciando Backend Django"
echo "===================================="
echo ""

# Activar entorno virtual
if [ -d "venv" ]; then
    source venv/bin/activate
else
    echo "[ERROR] Entorno virtual no encontrado"
    echo "Ejecuta primero: python -m venv venv"
    exit 1
fi

# Verificar que las dependencias estén instaladas
python -c "import django" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "[INFO] Instalando dependencias..."
    pip install -r requirements.txt
fi

# Ejecutar migraciones
echo "[INFO] Aplicando migraciones..."
python manage.py migrate

# Iniciar servidor
echo ""
echo "[INFO] Iniciando servidor en http://127.0.0.1:8000"
echo ""
python manage.py runserver



