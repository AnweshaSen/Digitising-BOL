import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

def extract_text_from_image(image):
    text = pytesseract.image_to_string(image)
    return text
