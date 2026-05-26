@echo off
REM Script para subir proyecto a GitHub
REM Ejecutar como: git_push.bat

echo.
echo ════════════════════════════════════════════════════════════════
echo PDF to Word Converter - Subir a GitHub
echo ════════════════════════════════════════════════════════════════
echo.

REM Verificar si Git está instalado
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ ERROR: Git no está instalado
    echo Por favor instala desde: https://git-scm.com/download/win
    pause
    exit /b 1
)

REM Verificar si estamos en repositorio Git
if not exist .git (
    echo.
    echo ⚠️  No estás en un repositorio Git
    echo.
    echo ¿Deseas inicializar uno? (S/N)
    set /p init_repo=
    
    if /i "%init_repo%"=="S" (
        echo.
        echo Inicializando Git...
        git init
        echo.
        echo Ingresa tu URL de repositorio GitHub
        echo (Ejemplo: https://github.com/usuario/pdf-to-word-converter.git)
        set /p repo_url=
        git remote add origin !repo_url!
        echo ✓ Repositorio inicializado
    ) else (
        echo Abortado.
        pause
        exit /b 1
    )
)

echo.
echo Mostrando estado actual...
git status
echo.

REM Agregar archivos
echo.
echo Agregando archivos...
git add .

REM Mensaje de commit
echo.
echo ════════════════════════════════════════════════════════════════
echo Ingresa el mensaje del commit (ejemplo: "Add new features")
set /p commit_msg=
echo ════════════════════════════════════════════════════════════════
echo.

if "%commit_msg%"=="" (
    set commit_msg=Update project files
)

REM Hacer commit
echo Creando commit: "%commit_msg%"
git commit -m "%commit_msg%"

if %errorlevel% neq 0 (
    echo.
    echo ⚠️  No hay cambios para commitar (todo ya está actualizado)
    echo.
    pause
    exit /b 0
)

REM Push
echo.
echo Subiendo a GitHub...
git push origin main

if %errorlevel% neq 0 (
    echo.
    echo ❌ ERROR al subir a GitHub
    echo Posibles causas:
    echo   1. No tienes permiso (token expirado)
    echo   2. Rama incorrecta (no es 'main')
    echo   3. Problemas de conexión
    echo.
    pause
    exit /b 1
)

echo.
echo ════════════════════════════════════════════════════════════════
echo ✓ ÉXITO: Proyecto subido a GitHub correctamente
echo ════════════════════════════════════════════════════════════════
echo.
echo Próximos pasos:
echo   1. Ve a Render: https://dashboard.render.com
echo   2. Crea nuevo "Web Service"
echo   3. Conecta tu repositorio GitHub
echo   4. Elige plan (Free o Starter)
echo   5. ¡Tu app estará en línea en 5-10 minutos!
echo.

pause
