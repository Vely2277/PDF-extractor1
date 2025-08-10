import os
import tempfile
import logging
from flask import Flask, request, jsonify
from werkzeug.middleware.proxy_fix import ProxyFix

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    from pdfminer.high_level import extract_text
    PDFMINER_AVAILABLE = True
    logger.info("pdfminer.six available")
except ImportError:
    PDFMINER_AVAILABLE = False
    logger.warning("pdfminer.six not available")

try:
    from pdf2image import convert_from_path
    import pytesseract
    OCR_AVAILABLE = True
    logger.info("OCR dependencies available")
except ImportError:
    OCR_AVAILABLE = False
    logger.warning("OCR dependencies not available")

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

@app.route('/extract', methods=['POST'])
def extract_pdf():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    file = request.files['file']
    if not file.filename or not file.filename.lower().endswith('.pdf'):
        return jsonify({'error': 'Only PDF files are supported'}), 400
    
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp:
        file.save(tmp.name)
        
        # Try text extraction first
        text = ""
        method_used = "none"
        
        if PDFMINER_AVAILABLE:
            try:
                logger.info("Attempting text extraction with pdfminer")
                text = extract_text(tmp.name)
                if text and text.strip():
                    method_used = "pdfminer"
                    logger.info(f"Successfully extracted {len(text)} characters with pdfminer")
                else:
                    logger.info("pdfminer returned empty text, trying OCR")
            except Exception as e:
                logger.error(f"pdfminer extraction failed: {e}")
                text = ""
        
        if not text.strip() and OCR_AVAILABLE:
            # If no text found, try OCR
            try:
                logger.info("Starting OCR processing")
                images = convert_from_path(tmp.name, dpi=300)
                logger.info(f"Converted PDF to {len(images)} images")
                ocr_text = ""
                for i, image in enumerate(images):
                    logger.info(f"Processing page {i+1} with OCR")
                    page_text = pytesseract.image_to_string(image, lang='eng')
                    logger.info(f"Page {i+1} extracted {len(page_text)} characters")
                    ocr_text += page_text + "\n"
                text = ocr_text
                if text.strip():
                    method_used = "ocr"
                    logger.info(f"Successfully extracted {len(text)} characters with OCR")
                else:
                    logger.warning("OCR returned empty text")
            except Exception as e:
                logger.error(f"OCR extraction failed: {e}")
                text = ""
        
        os.unlink(tmp.name)
    
    if not text.strip():
        return jsonify({'error': 'No text could be extracted from the PDF'}), 400
    
    return jsonify({
        'success': True,
        'text': text.strip(),
        'method': method_used
    })

@app.route('/')
def home():
    return 'PDF Extraction API is running.'

@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'service': 'PDF Text Extractor'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)