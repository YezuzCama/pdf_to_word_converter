# PDF to Word Converter - Guía rápida de instalación

## ⚡ Quick Start (Inicio Rápido)

### 1. Descargar e instalar Tesseract OCR

**Windows:**

1. Ir a: https://github.com/UB-Mannheim/tesseract/wiki
2. Descargar `tesseract-ocr-w64-setup-v5.x.x.exe`
3. Instalar en la ruta por defecto: `C:\Program Files\Tesseract-OCR`
4. ✓ Durante la instalación, mantener todas las opciones por defecto

**Mac:**

```bash
brew install tesseract
```

**Linux (Ubuntu/Debian):**

```bash
sudo apt-get install tesseract-ocr
```

---

### 2. Instalar dependencias Python

```bash
# Navegar a la carpeta del proyecto
cd pdf_to_word_converter

# Crear entorno virtual (recomendado)
python -m venv venv

# Activar entorno virtual
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Instalar librerías necesarias
pip install -r requirements.txt
```

---

### 3. Iniciar la aplicación

```bash
python main.py
```

Deberías ver:

```
Uvicorn running on http://127.0.0.1:8000
```

---

### 4. Abrir en navegador

```
http://localhost:8000
```

¡Listo! Ya puedes convertir tus PDFs a Word.

---

## 🔧 Solución de problemas

### Error: "pytesseract.TesseractNotFoundError"

**Solución:**

1. Abre `pdf_converter.py`
2. Agrega estas líneas al inicio del archivo:

```python
import pytesseract
# Configurar ruta de Tesseract (ajusta según tu ruta de instalación)
pytesseract.pytesseract.pytesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

### Error: "No module named 'pdf2image'"

**Solución:**

```bash
pip install --upgrade pdf2image
```

### El servidor no inicia

**Verifica que:**

- Python 3.8+ esté instalado: `python --version`
- El puerto 8000 no está en uso
- Todas las dependencias se instalaron correctamente

---

## 📝 Ejemplos de uso

### Conversión Simple

- Rápida y eficiente
- Solo extrae texto
- Perfecto para documentos con mucho texto

### Conversión Avanzada

- Preserva más formato
- Incluye imágenes de cada página
- Mejor para documentos con diseño especial

---

## 🆘 Contacto

Si tienes problemas:

1. Verifica que Tesseract esté correctamente instalado
2. Intenta reiniciar el servidor
3. Prueba con un PDF de prueba simple

¡Disfruta convirtiendo tus PDFs! 📄✨
