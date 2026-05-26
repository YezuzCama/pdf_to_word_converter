"""
Script de verificación del sistema para PDF to Word Converter
Verifica que todos los requisitos estén instalados
Ejecutar: python check_system.py
"""

import sys
import subprocess
from pathlib import Path

def check_python_version():
    """Verificar versión de Python"""
    print("\n📌 Verificando Python...")
    version = sys.version_info
    
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print(f"  ❌ Python 3.8+ requerido (tienes {version.major}.{version.minor})")
        return False
    else:
        print(f"  ✓ Python {version.major}.{version.minor} ✓")
        return True

def check_pip():
    """Verificar pip"""
    print("\n📌 Verificando pip...")
    try:
        result = subprocess.run([sys.executable, "-m", "pip", "--version"], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print(f"  ✓ pip instalado")
            return True
    except:
        pass
    
    print("  ❌ pip no encontrado")
    return False

def check_module(module_name, package_name=None):
    """Verificar si un módulo Python está instalado"""
    if package_name is None:
        package_name = module_name
    
    try:
        __import__(module_name)
        print(f"  ✓ {package_name} instalado")
        return True
    except ImportError:
        print(f"  ❌ {package_name} NO instalado")
        return False

def check_python_packages():
    """Verificar librerías Python necesarias"""
    print("\n📌 Verificando librerías Python...")
    
    packages = [
        ('fastapi', 'FastAPI'),
        ('uvicorn', 'Uvicorn'),
        ('docx', 'python-docx'),
        ('pdf2image', 'pdf2image'),
        ('pytesseract', 'pytesseract'),
        ('PIL', 'Pillow'),
        ('aiofiles', 'aiofiles'),
        ('pydantic', 'Pydantic'),
    ]
    
    results = []
    for module, name in packages:
        results.append(check_module(module, name))
    
    return all(results)

def check_tesseract():
    """Verificar Tesseract OCR"""
    print("\n📌 Verificando Tesseract OCR...")
    
    try:
        result = subprocess.run(["tesseract", "--version"], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            version_line = result.stdout.split('\n')[0]
            print(f"  ✓ Tesseract instalado ({version_line.strip()})")
            return True
    except FileNotFoundError:
        pass
    
    print("  ⚠️  Tesseract OCR NO encontrado")
    print("     Descárgalo de: https://github.com/UB-Mannheim/tesseract/wiki")
    return False

def check_poppler():
    """Verificar Poppler (para pdf2image)"""
    print("\n📌 Verificando Poppler...")
    
    try:
        result = subprocess.run(["pdftoppm", "--version"], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print(f"  ✓ Poppler instalado")
            return True
    except FileNotFoundError:
        pass
    
    print("  ⚠️  Poppler NO encontrado")
    print("     En Windows, se instala automáticamente con pdf2image")
    print("     Si hay problemas, descárgalo de: https://github.com/oschwartz10612/poppler-windows/releases/")
    return False

def check_directories():
    """Verificar directorios del proyecto"""
    print("\n📌 Verificando directorios...")
    
    dirs = [
        (Path("static"), "Carpeta static"),
        (Path("uploads"), "Carpeta uploads (se crea automáticamente)"),
        (Path("outputs"), "Carpeta outputs (se crea automáticamente)"),
    ]
    
    results = []
    for dir_path, desc in dirs:
        if dir_path.exists():
            print(f"  ✓ {desc}")
            results.append(True)
        else:
            print(f"  ⚠️  {desc} - se creará automáticamente")
            results.append(True)
    
    return all(results)

def check_files():
    """Verificar archivos principales"""
    print("\n📌 Verificando archivos...")
    
    files = [
        (Path("main.py"), "Aplicación principal"),
        (Path("pdf_converter.py"), "Módulo de conversión"),
        (Path("requirements.txt"), "Dependencias"),
        (Path("static/index.html"), "Interfaz web"),
    ]
    
    results = []
    for file_path, desc in files:
        if file_path.exists():
            print(f"  ✓ {desc}")
            results.append(True)
        else:
            print(f"  ❌ {desc} - NO ENCONTRADO")
            results.append(False)
    
    return all(results)

def main():
    """Ejecutar todas las verificaciones"""
    print("\n" + "="*60)
    print("PDF to Word Converter - Verificación de Sistema")
    print("="*60)
    
    checks = [
        ("Python", check_python_version()),
        ("pip", check_pip()),
        ("Librerías Python", check_python_packages()),
        ("Tesseract OCR", check_tesseract()),
        ("Poppler", check_poppler()),
        ("Directorios", check_directories()),
        ("Archivos", check_files()),
    ]
    
    print("\n" + "="*60)
    print("RESUMEN")
    print("="*60)
    
    all_ok = True
    for name, result in checks:
        status = "✓" if result else "❌"
        print(f"{status} {name}")
        if not result:
            all_ok = False
    
    print("="*60)
    
    if all_ok:
        print("\n🎉 ¡Todo está correctamente configurado!")
        print("\nPara ejecutar la app:")
        print("  1. Activa el entorno virtual: venv\\Scripts\\activate")
        print("  2. Ejecuta: python main.py")
        print("  3. Abre: http://localhost:8000")
        return 0
    else:
        print("\n⚠️  Hay algunos problemas que resolver")
        print("\nPasos recomendados:")
        print("  1. Instala Tesseract OCR si no está instalado")
        print("  2. Ejecuta: pip install -r requirements.txt")
        print("  3. Vuelve a ejecutar este script")
        return 1

if __name__ == "__main__":
    sys.exit(main())
