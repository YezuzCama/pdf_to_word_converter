@echo off
REM Script de instalación automática para PDF to Word Converter
REM Ejecutar como: install.bat

echo.
echo ========================================
echo PDF to Word Converter - Instalador
echo ========================================
echo.

REM Verificar si Python está instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ ERROR: Python no está instalado o no está en el PATH
    echo Por favor, instala Python desde: https://www.python.org
    pause
    exit /b 1
)

echo ✓ Python detectado

REM Crear entorno virtual
echo.
echo Creando entorno virtual...
if exist venv (
    echo Entorno virtual ya existe. Saltando...
) else (
    python -m venv venv
    echo ✓ Entorno virtual creado
)

REM Activar entorno virtual
echo.
echo Activando entorno virtual...
call venv\Scripts\activate.bat

REM Instalar dependencias
echo.
echo Instalando dependencias... (esto puede tardar unos minutos)
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo ❌ ERROR: Fallo la instalación de dependencias
    pause
    exit /b 1
)

echo ✓ Dependencias instaladas

REM Verificar Tesseract
echo.
echo Verificando Tesseract OCR...
tesseract --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ⚠️  ADVERTENCIA: Tesseract OCR no detectado
    echo.
    echo Tesseract es REQUERIDO para que la app funcione.
    echo Descárgalo de: https://github.com/UB-Mannheim/tesseract/wiki
    echo.
    echo Continuar sin Tesseract no funcionará correctamente.
    echo Pulsa cualquier tecla para continuar o Ctrl+C para cancelar...
    pause
) else (
    echo ✓ Tesseract detectado
)

echo.
echo ========================================
echo ✓ Instalación completada correctamente
echo ========================================
echo.
echo Para ejecutar la app:
echo   1. venv\Scripts\activate.bat
echo   2. python main.py
echo   3. Abre: http://localhost:8000
echo.
pause
