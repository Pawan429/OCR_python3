from PIL import Image
import pytesseract

# pytesseract.pytesseract.tesseract_cmd = "usr/appdata/local/programs/site-pakages/python/python36/lib/pytesseract/pytesseract.py"
print(pytesseract.image_to_string(Image.open('text.jpg')))