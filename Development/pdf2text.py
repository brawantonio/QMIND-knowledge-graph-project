#pdf2text.py
# Vanya Kootchin
# January 11th, 2022

"""Library for reading PDFs into python data structures

   Requires 'pdfplumber' library...
   
        - pip install pdfplumber
        
    ...for whichever virtual environment you're using

"""

import re
import sys  

try: # pdfplumber
  import pdfplumber
except:
  print('Error:\tpdfplumber library has not been installed.\n\tTry \'pip install pdfplumber\' in venv.')
  sys.exit(0)

def readPDF(fp, arg=0):
    """A function for reading a given pdf and returning the pages 
    as a string or object in python

    Args:
        fp (string): The path to the PDF intended for reading
        arg (int)  : defines the return type using text cleaning inately, 0 or no arguement gives raw text, 1 gives pdf object
        
    Returns:
        list: The list of sentences in the pdf
    """
    lines = []
    with pdfplumber.open(fp) as pdf:
        for page in pdf.pages:
            parag = re.split(u'\n(?=\u2022|[A-Z])', page.extract_text())
            for block in parag:
                  sentences = block.split('.')
                  for i in range(len(sentences)):
                        sentences[i] = sentences[i].strip()
                        sentences[i] = sentences[i].replace('\n', '')
                        sentences[i] = sentences[i].replace('  ', ' ')
                  lines.extend(sentences)
    
    while('' in lines):
      lines.remove('') # getting rid of space lines
    
    return lines

