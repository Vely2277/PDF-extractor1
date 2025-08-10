# Overview

A Flask-based API service for PDF text extraction with OCR fallback, optimized for deployment on platforms like Render. The application provides a simple JSON API that extracts text from uploaded PDF files using pdfminer.six as the primary method, with automatic fallback to OCR (pdf2image + pytesseract) for scanned documents. The service is deployment-ready with comprehensive error handling and health monitoring endpoints.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Backend Framework
- **Flask Application**: Single-file Flask app (`app.py`) with a separate entry point (`main.py`)
- **File Upload Handling**: Supports PDF files up to 16MB with secure filename validation
- **Dual Response Format**: Handles both web form submissions and JSON API requests

## Text Extraction Engine
- **Primary Method**: pdfminer.six for direct text extraction from searchable PDFs
- **Fallback Method**: OCR pipeline using pdf2image + pytesseract + PIL for scanned documents
- **Graceful Degradation**: System continues to function even if OCR dependencies are unavailable
- **Error Handling**: Comprehensive logging and error reporting throughout the extraction pipeline

## Frontend Design
- **Bootstrap Dark Theme**: Modern, responsive UI using Replit's bootstrap-agent-dark-theme
- **Progressive Enhancement**: Form works with and without JavaScript
- **Visual Feedback**: Font Awesome icons, loading animations, and flash messages for user feedback
- **Accessibility**: Proper form labels, semantic HTML structure

## File Processing Strategy
- **Temporary File Handling**: Uses secure temporary files for processing uploads
- **Memory Management**: Streams file processing to avoid memory issues with large PDFs
- **Security**: Filename sanitization and file type validation

# External Dependencies

## Core Dependencies
- **Flask**: Web framework with ProxyFix middleware for deployment
- **Werkzeug**: File upload utilities and secure filename handling

## PDF Processing
- **pdfminer.six**: Primary text extraction from PDF documents
- **pdf2image**: Converts PDF pages to images for OCR processing
- **pytesseract**: OCR engine for text recognition from images
- **Pillow (PIL)**: Image processing library for OCR pipeline

## Frontend Assets
- **Bootstrap**: UI framework (via Replit CDN)
- **Font Awesome**: Icon library for visual elements
- **Custom CSS**: Application-specific styling enhancements

## Development Tools
- **Python Logging**: Comprehensive logging throughout the application
- **Tempfile**: Secure temporary file handling for uploads