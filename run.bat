@echo off
REM Script para ejecutar PDF to Word Converter
echo.
echo ========================================
echo PDF to Word Converter
echo ========================================
echo.

REM Verificar si entorno virtual existe
if not exist venv (
    echo ❌ Entorno virtual no encontrado
    echo Por favor ejecuta: install.bat
    pause
    exit /b 1
)

REM Activar entorno virtual
call venv\Scripts\activate.bat

REM Verificar Tesseract
tesseract --version >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo ⚠️  ADVERTENCIA: Tesseract OCR no encontrado
    echo La app no funcionará correctamente sin Tesseract.
    echo Descárgalo de: https://github.com/UB-Mannheim/tesseract/wiki
    echo.
)

echo ✓ Iniciando servidor...
echo.
echo 🌐 Abre tu navegador en: http://localhost:8000
echo.
echo Para detener el servidor: Presiona Ctrl+C
echo.

REM Iniciar FastAPI
python main.py

pause
