#img2text.py

from PIL import Image
import pytesseract

# Include tesseract executable in your path
#pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def TextFromImage(path):
    # Create an image object of PIL library
    image = Image.open(path)
    # pass image into pytesseract module
    # pytesseract is trained in many languages
    image_to_text = pytesseract.image_to_string(image, lang='eng')
    return image_to_text

#test1 = TextFromImage('C:/Users/trist/OneDrive/Queens 21-22/QMIND/Knowledge_Graph/test_image_1.jpg')
#test2 = TextFromImage('C:/Users/trist/OneDrive/Queens 21-22/QMIND/Knowledge_Graph/test_image_2.png')

#print('\n----------------------------\n',test1,'\n----------------------------\n',test2,'\n----------------------------\n')