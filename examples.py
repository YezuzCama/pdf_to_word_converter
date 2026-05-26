"""
Ejemplos de cómo usar la API de PDF to Word Converter
Ejecutar: python examples.py
"""

import requests
import time
from pathlib import Path

# URL del servidor (cambiar si está en otro servidor)
API_URL = "http://localhost:8000/api/convert"

def ejemplo_1_conversion_simple():
    """Ejemplo 1: Convertir PDF con modo simple"""
    print("\n" + "="*50)
    print("Ejemplo 1: Conversión Simple")
    print("="*50)
    
    # Ruta del PDF a convertir
    pdf_file = Path("documento_prueba.pdf")
    
    if not pdf_file.exists():
        print(f"❌ Archivo no encontrado: {pdf_file}")
        print("Por favor coloca un PDF de prueba en la carpeta del proyecto")
        return
    
    try:
        print(f"📄 Convertiendo: {pdf_file.name}")
        
        with open(pdf_file, 'rb') as f:
            files = {'file': f}
            data = {'mode': 'simple'}
            
            response = requests.post(API_URL, files=files, data=data)
        
        if response.status_code == 200:
            # Guardar archivo descargado
            output_file = f"{pdf_file.stem}_simple.docx"
            with open(output_file, 'wb') as f:
                f.write(response.content)
            print(f"✓ Éxito! Guardado como: {output_file}")
        else:
            print(f"❌ Error: {response.status_code}")
            print(response.json())
    
    except Exception as e:
        print(f"❌ Error: {e}")

def ejemplo_2_conversion_avanzada():
    """Ejemplo 2: Convertir PDF con modo avanzado"""
    print("\n" + "="*50)
    print("Ejemplo 2: Conversión Avanzada")
    print("="*50)
    
    pdf_file = Path("documento_prueba.pdf")
    
    if not pdf_file.exists():
        print(f"❌ Archivo no encontrado: {pdf_file}")
        return
    
    try:
        print(f"📄 Convertiendo: {pdf_file.name} (modo avanzado)")
        
        with open(pdf_file, 'rb') as f:
            files = {'file': f}
            data = {'mode': 'advanced'}  # Cambiar a 'advanced'
            
            response = requests.post(API_URL, files=files, data=data)
        
        if response.status_code == 200:
            output_file = f"{pdf_file.stem}_advanced.docx"
            with open(output_file, 'wb') as f:
                f.write(response.content)
            print(f"✓ Éxito! Guardado como: {output_file}")
        else:
            print(f"❌ Error: {response.status_code}")
    
    except Exception as e:
        print(f"❌ Error: {e}")

def ejemplo_3_procesar_multiples():
    """Ejemplo 3: Procesar múltiples PDFs"""
    print("\n" + "="*50)
    print("Ejemplo 3: Procesar Múltiples PDFs")
    print("="*50)
    
    # Buscar todos los PDFs en la carpeta
    pdf_files = list(Path(".").glob("*.pdf"))
    
    if not pdf_files:
        print("❌ No hay archivos PDF en esta carpeta")
        return
    
    print(f"📦 Encontrados {len(pdf_files)} PDFs")
    
    for i, pdf_file in enumerate(pdf_files, 1):
        print(f"\n[{i}/{len(pdf_files)}] Procesando: {pdf_file.name}")
        
        try:
            with open(pdf_file, 'rb') as f:
                files = {'file': f}
                data = {'mode': 'simple'}
                
                response = requests.post(API_URL, files=files, data=data)
            
            if response.status_code == 200:
                output_file = f"{pdf_file.stem}_converted.docx"
                with open(output_file, 'wb') as f:
                    f.write(response.content)
                print(f"  ✓ Guardado como: {output_file}")
            else:
                print(f"  ❌ Error: {response.status_code}")
        
        except Exception as e:
            print(f"  ❌ Error: {e}")
        
        # Pequeña pausa entre peticiones
        time.sleep(1)
    
    print(f"\n✓ Completado!")

def ejemplo_4_verificar_servidor():
    """Ejemplo 4: Verificar si el servidor está funcionando"""
    print("\n" + "="*50)
    print("Ejemplo 4: Verificar Servidor")
    print("="*50)
    
    try:
        response = requests.get("http://localhost:8000/health", timeout=5)
        if response.status_code == 200:
            print(f"✓ Servidor está en línea")
            print(f"  Status: {response.json()}")
        else:
            print(f"❌ Servidor respondió con error: {response.status_code}")
    
    except requests.ConnectionError:
        print("❌ No se puede conectar al servidor")
        print("   Asegúrate de que esté ejecutando: python main.py")
    
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("\n🚀 PDF to Word Converter - Ejemplos de API")
    print("\nSelecciona un ejemplo para ejecutar:")
    print("1. Conversión simple")
    print("2. Conversión avanzada")
    print("3. Procesar múltiples PDFs")
    print("4. Verificar servidor")
    print("0. Salir")
    
    while True:
        choice = input("\nIngresa tu opción (0-4): ").strip()
        
        if choice == "1":
            ejemplo_1_conversion_simple()
        elif choice == "2":
            ejemplo_2_conversion_avanzada()
        elif choice == "3":
            ejemplo_3_procesar_multiples()
        elif choice == "4":
            ejemplo_4_verificar_servidor()
        elif choice == "0":
            print("\n¡Hasta luego! 👋")
            break
        else:
            print("❌ Opción inválida")
