#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Pip installs
get_ipython().system('pip install docx2txt')
get_ipython().system('pip install pdfplumber')
get_ipython().system('pip install pytesseract')


# In[24]:


# Imports
import docx2txt
from PDFReader import *
from img2txt import *


# In[27]:


# Test extracting text from docx
# Note: Images will be stored in current directoy
print(docx2txt.process("./test_files/TestDoc1.docx", "./"))


# In[19]:


# Test PDFReader
print(printPDF(readPDF("./test_files/Test1PDF.pdf")))


# In[28]:


# Test img2txt
pytesseract.pytesseract.tesseract_cmd = "./tesseract.exe"

print(TextFromImage("./test_files/test_image_1.jpg"))


# In[ ]:




