# Notas importantes para Windows

## ⚠️ Instalación de Tesseract OCR

Tesseract es **OBLIGATORIO** para que la app funcione. Sin él, OCR no funcionará.

### Pasos:

1. **Descargar installer:**
   - Ir a: https://github.com/UB-Mannheim/tesseract/wiki
   - Descargar: `tesseract-ocr-w64-setup-v5.x.x.exe` (versión más reciente)

2. **Instalar:**
   - Ejecutar el .exe
   - Aceptar términos
   - **Mantener ruta por defecto:** `C:\Program Files\Tesseract-OCR`
   - Marcar todas las opciones de idiomas deseados

3. **Verificar instalación:**
   ```bash
   # Abrir Command Prompt (cmd) o PowerShell
   tesseract --version
   ```
   Debería mostrar la versión instalada.

---

## ✅ Instalación rápida de dependencias

```bash
# 1. En la carpeta del proyecto
cd pdf_to_word_converter

# 2. Crear entorno virtual
python -m venv venv
venv\Scripts\activate

# 3. Instalar todo de una vez
pip install fastapi uvicorn python-docx pdf2image pytesseract pillow aiofiles python-multipart pydantic
```

---

## 🚀 Ejecutar la app

```bash
# Activar entorno virtual
venv\Scripts\activate

# Iniciar servidor
python main.py
```

Abre: `http://localhost:8000`

---

## 💾 Carpetas que se crean automáticamente

```
pdf_to_word_converter/
├── uploads/     ← PDFs subidos (se eliminan después de procesar)
└── outputs/     ← Word generados (.docx)
```

Los archivos Word descargados se guardan en tu carpeta de Descargas.

---

## 🔍 Cómo verificar que todo funciona

1. Instala dependencias
2. Ejecuta `python main.py`
3. Abre `http://localhost:8000`
4. Sube un PDF de prueba pequeño
5. Haz clic en "Convertir a Word"
6. Descarga el archivo .docx

Si no hay errores = ¡Todo está bien! ✓

---

## ❌ Errores comunes y soluciones

| Error                                            | Causa                       | Solución                         |
| ------------------------------------------------ | --------------------------- | -------------------------------- |
| `TesseractNotFoundError`                         | Tesseract no instalado      | Instalar desde GitHub            |
| `No module named 'pdf2image'`                    | Librería no instalada       | `pip install pdf2image`          |
| `ModuleNotFoundError: No module named 'fastapi'` | Entorno virtual no activado | Ejecutar `venv\Scripts\activate` |
| Puerto 8000 en uso                               | Otra app usa ese puerto     | Cambiar puerto en `main.py`      |

---

## 🆘 Si nada funciona

1. **Reinstala Tesseract:**
   - Desinstalar completamente
   - Reiniciar PC
   - Reinstalar desde: https://github.com/UB-Mannheim/tesseract/wiki

2. **Reinstala dependencias:**

   ```bash
   pip uninstall fastapi uvicorn python-docx pdf2image pytesseract pillow -y
   pip install -r requirements.txt
   ```

3. **Prueba con Python limpio:**

   ```bash
   # Eliminar carpeta venv
   rmdir /s /q venv

   # Crear nueva
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

---

Pregunta en el README.md si necesitas más ayuda.
