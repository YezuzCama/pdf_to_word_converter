"""
Configuración de la aplicación PDF to Word Converter
Modifica estos valores según tus necesidades
"""

import os
from pathlib import Path

# ==================== DIRECTORIOS ====================
BASE_DIR = Path(__file__).parent
UPLOAD_DIR = BASE_DIR / "uploads"
OUTPUT_DIR = BASE_DIR / "outputs"

# Crear directorios si no existen
UPLOAD_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

# ==================== CONFIGURACIÓN DEL SERVIDOR ====================
HOST = "0.0.0.0"
PORT = 8000
DEBUG = False  # Cambiar a True para desarrollo

# ==================== CONFIGURACIÓN DE ARCHIVOS ====================
MAX_FILE_SIZE_MB = 50  # Tamaño máximo de PDF en MB
ALLOWED_EXTENSIONS = {".pdf"}
UPLOAD_TIMEOUT = 300  # segundos

# ==================== OCR Y PROCESAMIENTO ====================
# Idiomas para OCR (tesseract)
OCR_LANGUAGES = "spa+eng"  # Español + Inglés

# Calidad de PDF a imagen (más alto = mejor pero más lento)
DPI = 200  # 150-300 recomendado

# Borrar archivos temporales después de procesar
CLEANUP_TEMP_FILES = True

# ==================== TESSERACT CONFIGURACIÓN ====================
# Descomentar si Tesseract no está en el PATH
# import pytesseract
# pytesseract.pytesseract.pytesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# ==================== CONVERSIÓN DE DOCUMENTOS ====================
# Fuente para documentos Word
WORD_FONT_NAME = "Calibri"
WORD_FONT_SIZE = 11

# Tamaño de línea en documentos Word (1.0, 1.15, 1.5, 2.0)
WORD_LINE_SPACING = 1.15

# Ancho máximo de imágenes en documentos Word (en pulgadas)
MAX_IMAGE_WIDTH = 5

# ==================== CORS ====================
CORS_ORIGINS = ["*"]  # En producción, especificar dominios reales

# ==================== LOGGING ====================
LOG_LEVEL = "INFO"  # DEBUG, INFO, WARNING, ERROR
LOG_FILE = BASE_DIR / "app.log"

# ==================== LÍMITES ====================
# Número máximo de páginas a procesar (0 = ilimitado)
MAX_PAGES = 0

# Esperar entre procesamiento de archivos (segundos) - 0 para sin limite
RATE_LIMIT_SECONDS = 0

# ==================== CARACTERÍSTICAS ====================
ENABLE_SIMPLE_MODE = True
ENABLE_ADVANCED_MODE = True
ENABLE_IMAGE_THUMBNAILS = True
ENABLE_COMPRESSION = False  # Comprimir documento final

# ==================== ALMACENAMIENTO ====================
# Retener archivos generados por (horas) - 0 para indefinido
KEEP_OUTPUT_FILES_HOURS = 24

# Eliminar automáticamente archivos de entrada
AUTO_DELETE_UPLOADS = True
AUTO_DELETE_OUTPUTS = False  # Cambiar a True si tienes espacio limitado
