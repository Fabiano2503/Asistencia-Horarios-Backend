@echo off
echo ====================================
echo   Iniciando Backend Django
echo ====================================
echo.

REM Activar entorno virtual
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
) else (
    echo [ERROR] Entorno virtual no encontrado
    echo Ejecuta primero: python -m venv venv
    pause
    exit /b 1
)

REM Verificar que las dependencias esten instaladas
python -c "import django" 2>nul
if errorlevel 1 (
    echo [INFO] Instalando dependencias...
    pip install -r requirements.txt
)

REM Ejecutar migraciones
echo [INFO] Aplicando migraciones...
python manage.py migrate

REM Iniciar servidor
echo.
echo [INFO] Iniciando servidor en http://127.0.0.1:8000
echo.
python manage.py runserver

pause



