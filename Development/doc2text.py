#doc2text.py

import os, time
from pwd import getpwuid
import sys
import re
from PIL import Image

#-----------checking for dependencies--------------------------
try: #docx2txt
    import docx2txt
except:
    print('Error:\tdocx2txt library has not been installed.\n\tTry \'pip install docx2txt\'.')
    sys.exit(0)

try: # pdfplumber
    import pdfplumber
except:
    print('Error:\tpdfplumber library has not been installed.\n\tTry \'pip install pdfplumber\' in venv.')
    sys.exit(0)

try: # cv2
    import cv2
except:
    print('Error:\cv2 library has not been installed.\n\tTry \'pip install cv2\' in venv.')
    sys.exit(0)

try: 
    import pytesseract
except:
    print('Error:\cv2 library has not been installed.\n\tTry \'pip install pytesseract\' in venv.')
    sys.exit(0)
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/Cellar/tesseract/5.0.1/bin/tesseract'

#----------class to extract metadata ------------------------------------------------------------
class metadata:
    def __init__(self, filepath):
        self.owner = getpwuid(os.stat(filepath).st_uid).pw_name
        self.ext = os.path.splitext(filepath)[1]
        self.size = os.path.getsize(filepath)
        self.date_mod = time.ctime(os.path.getmtime(filepath))
        self.date_cre = time.ctime(os.path.getctime(filepath)) 
    
    def all(self):
        string = ""
        for attribute, value in self.__dict__.items():
            string = string + attribute + ": " + str(value) + '\n'
        return string

#----------- function to extract text from a docx document---------------------------------------

def docx2text(filepath, save_img = False):
    dirpath = os.path.dirname(filepath)
    if save_img:
        if os.path.isdir(dirpath+'/temp_images_dir')==False:
            os.mkdir(dirpath+'/temp_images_dir')
        return docx2txt.process(filepath, dirpath+'/temp_images_dir')
    else: return docx2txt.process(filepath)

#--------------function to extract text from a pdf---------------------------------------------

def pdf2text(filepath):
	pdf = pdfplumber.open(filepath)
	string = ""
	for page in pdf.pages:
		string = string+ page.extract_text()
	return string

#------------------- function to extract text from images -------------------------------------

def img2text(filepath, preprocessing = False):
    if preprocessing:
        return   
    image = cv2.imread(filepath,0)
    return pytesseract.image_to_string(image)


#--------------------- scan files in directory ----------------------------------------------

def get_files(filepath):
    extensions = ['.docx', '.pdf', '.png', '.jpeg', '.jpg'] #always docx and pdf in first place

    onlyfiles = [f for f in os.listdir(filepath) if os.path.isfile(os.path.join(filepath, f)) ]
    onlyfiles = [f for f in os.listdir(filepath) if not f=='.DS_Store' ]
    files_in_dir = {}
    files_in_dir['docx'] = [f for f in onlyfiles if os.path.splitext(f)[1] in extensions[0]]
    files_in_dir['pdf'] = [f for f in onlyfiles if os.path.splitext(f)[1] in extensions[1]]
    files_in_dir['img'] = [f for f in onlyfiles if os.path.splitext(f)[1] in extensions[2:]]
    
    return files_in_dir

#----------------------- # function to decide which method to use --------------------------
def extract_text(filepath,key):
    if key == 'docx': return docx2text(filepath)
    if key == 'pdf': return pdf2text(filepath)
    if key == 'img': return img2text(filepath)

