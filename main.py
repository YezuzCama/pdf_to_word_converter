from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import tempfile
import os
from pdf_converter import PDFConverter

app = FastAPI(title="PDF to Word Converter")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create uploads and output directories
UPLOAD_DIR = Path("uploads")
OUTPUT_DIR = Path("outputs")
UPLOAD_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

converter = PDFConverter()

@app.post("/api/convert")
async def convert_pdf(
    file: UploadFile = File(...),
    mode: str = Form("simple")
):
    """
    Convert PDF to Word document.
    
    Args:
        file: PDF file to convert
        mode: 'simple' for text extraction, 'advanced' for format preservation
    
    Returns:
        Word document file
    """
    if not file.filename.lower().endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files are accepted")
    
    try:
        # Save uploaded file temporarily
        temp_path = UPLOAD_DIR / file.filename
        with open(temp_path, 'wb') as f:
            content = await file.read()
            f.write(content)
        
        # Convert based on mode
        if mode == "advanced":
            output_path = converter.convert_advanced(str(temp_path))
        else:
            output_path = converter.convert_simple(str(temp_path))
        
        return FileResponse(
            output_path,
            media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            filename=output_path.name
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error converting PDF: {str(e)}")
    
    finally:
        # Clean up temporary files
        if temp_path.exists():
            temp_path.unlink()

@app.get("/")
async def root():
    """Serve the main page"""
    return FileResponse("static/index.html")

@app.get("/health")
async def health():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
