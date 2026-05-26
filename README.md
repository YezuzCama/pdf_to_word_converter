# PDF to Word Converter

Aplicación web para convertir PDFs a documentos Word editables.

## Características

✨ **Dos modos de conversión:**

- **Simple**: Extrae texto mediante OCR (Tesseract)
- **Avanzado**: Intenta preservar formato y agrega miniaturas de páginas

🎨 **Interfaz moderna con:**

- Drag & drop para cargar archivos
- Vista previa antes de convertir
- Indicadores de progreso
- Descarga automática del archivo Word

⚙️ **Tecnología:**

- Backend: FastAPI (Python)
- Frontend: HTML5 + CSS3 + JavaScript puro (sin dependencias)
- Librerías: pdf2image, pytesseract, python-docx

## Instalación

### Requisitos previos

- Python 3.8+
- Poppler (para pdf2image): https://github.com/oschwartz10612/poppler-windows/releases/
- Tesseract OCR: https://github.com/UB-Mannheim/tesseract/wiki

### Pasos

1. **Clonar/Descargar el proyecto**

```bash
cd pdf_to_word_converter
```

2. **Crear entorno virtual** (opcional pero recomendado)

```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

3. **Instalar dependencias**

```bash
pip install -r requirements.txt
```

4. **Configurar Tesseract** (en Windows)
   - Descargar e instalar desde: https://github.com/UB-Mannheim/tesseract/wiki
   - Actualizar la ruta en `pdf_converter.py` si es necesario:
   ```python
   pytesseract.pytesseract.pytesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
   ```

## Uso

1. **Iniciar servidor**

```bash
python main.py
```

2. **Abrir en navegador**

```
http://localhost:8000
```

3. **Convertir PDF:**
   - Selecciona modo (Simple o Avanzado)
   - Carga tu archivo PDF
   - Haz clic en "Convertir a Word"
   - Descarga automáticamente

## Estructura del proyecto

```
pdf_to_word_converter/
├── main.py              # Aplicación FastAPI principal
├── pdf_converter.py     # Lógica de conversión de PDFs
├── requirements.txt     # Dependencias Python
├── static/
│   └── index.html       # Interfaz web frontend
├── uploads/             # Archivos PDF subidos (temporal)
└── outputs/             # Documentos Word generados
```

## API Endpoints

### POST /api/convert

Convierte un archivo PDF a Word.

**Parameters:**

- `file` (FormData): Archivo PDF
- `mode` (FormData): 'simple' o 'advanced'

**Response:**

- Archivo Word (.docx)

**Ejemplo cURL:**

```bash
curl -X POST -F "file=@documento.pdf" -F "mode=advanced" http://localhost:8000/api/convert
```

## Notas importantes

⚠️ **OCR en Windows:**

- Asegúrate de tener Tesseract instalado correctamente
- La ruta por defecto es `C:\Program Files\Tesseract-OCR\tesseract.exe`

⚠️ **Rendimiento:**

- Archivos muy grandes pueden tardar más
- El modo avanzado es más lento por las imágenes adicionales

⚠️ **Calidad del OCR:**

- Depende de la calidad del PDF original
- PDFs escaneados requieren mejor resolución para mejor OCR

## Troubleshooting

**Error: "pytesseract.TesseractNotFoundError"**

- Verifica que Tesseract esté instalado
- Configura la ruta correcta en el código

**Error: "Module 'pdf2image' has no attribute 'convert_from_path'"**

- Reinstala pdf2image: `pip install --upgrade pdf2image`
- Verifica que Poppler esté en el PATH

**El OCR no reconoce bien el texto**

- Asegúrate que el PDF tenga buena calidad
- Prueba con `lang='spa+eng'` en pytesseract para otros idiomas

## Mejoras futuras

- [ ] Soporte para múltiples idiomas
- [ ] Procesar lotes de archivos
- [ ] Guardado en cloud (Google Drive, OneDrive)
- [ ] Edición en tiempo real del documento
- [ ] Mejora automática de imágenes escaneadas
- [ ] Autenticación y gestión de proyectos

## Licencia

MIT - Libre para uso personal y comercial

## Autor

Creado con ❤️ usando FastAPI y Python
