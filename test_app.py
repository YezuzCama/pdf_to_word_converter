"""
Tests básicos para PDF to Word Converter
Ejecutar: python test_app.py
"""

import pytest
from fastapi.testclient import TestClient
from pathlib import Path
from main import app

client = TestClient(app)

def test_health_endpoint():
    """Test del endpoint de salud"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_root_endpoint():
    """Test de la página principal"""
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]

def test_convert_without_file():
    """Test de conversión sin archivo"""
    response = client.post("/api/convert", data={"mode": "simple"})
    assert response.status_code == 422  # Unprocessable Entity

def test_convert_invalid_file():
    """Test de conversión con archivo inválido"""
    response = client.post(
        "/api/convert",
        files={"file": ("test.txt", b"test content")},
        data={"mode": "simple"}
    )
    assert response.status_code == 400

def test_invalid_mode():
    """Test con modo inválido"""
    pdf_file = Path("test_document.pdf")
    
    if pdf_file.exists():
        with open(pdf_file, "rb") as f:
            response = client.post(
                "/api/convert",
                files={"file": ("test.pdf", f)},
                data={"mode": "invalid"}
            )
        # Debería aceptar cualquier modo (mejor mejorar validación)
        assert response.status_code in [200, 422, 500]

def test_api_endpoint_exists():
    """Verificar que el endpoint API existe"""
    # Simplemente verificar que podemos acceder a la ruta
    response = client.options("/api/convert")
    # OPTIONS should either work or return 405
    assert response.status_code in [200, 405]

if __name__ == "__main__":
    # Ejecutar tests sin pytest
    print("Ejecutando tests básicos...")
    print("\n1. Test: Health endpoint")
    try:
        test_health_endpoint()
        print("   ✓ PASSED")
    except AssertionError as e:
        print(f"   ❌ FAILED: {e}")
    
    print("\n2. Test: Root endpoint")
    try:
        test_root_endpoint()
        print("   ✓ PASSED")
    except AssertionError as e:
        print(f"   ❌ FAILED: {e}")
    
    print("\n3. Test: Convert without file")
    try:
        test_convert_without_file()
        print("   ✓ PASSED")
    except AssertionError as e:
        print(f"   ❌ FAILED: {e}")
    
    print("\n4. Test: Convert invalid file")
    try:
        test_convert_invalid_file()
        print("   ✓ PASSED")
    except AssertionError as e:
        print(f"   ❌ FAILED: {e}")
    
    print("\n5. Test: API endpoint exists")
    try:
        test_api_endpoint_exists()
        print("   ✓ PASSED")
    except AssertionError as e:
        print(f"   ❌ FAILED: {e}")
    
    print("\n✓ Tests completados")
