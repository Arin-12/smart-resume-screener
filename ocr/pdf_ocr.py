from pdf2image import convert_from_path
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
POPPLER_PATH = r"C:\poppler-23.08.0\Library\bin"

def extract_text_from_pdf(pdf_path):
    try:
        pages = convert_from_path(
            pdf_path,
            dpi=300,
            poppler_path=POPPLER_PATH
        )
    except Exception as e:
        print("❌ PDF conversion failed:", e)
        print("👉 Tip: Convert PDF to image and use image OCR instead.")
        return ""

    full_text = ""
    for page in pages:
        text = pytesseract.image_to_string(page, config="--oem 3 --psm 6")
        full_text += text + "\n"

    return full_text
