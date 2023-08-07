from PIL import Image
from pytesseract import pytesseract

    
windows_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

path_to_image = 'images\Screenshot_1.png'

pytesseract.tesseract_cmd = windows_path
    
img = Image.open(path_to_image)

extracted_text = pytesseract.image_to_string(img)

print(extracted_text)
