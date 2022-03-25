# Vanya Kootchin
# January 12th, 2022

"""
This script illustrates how to implement the functions from 'PDFReader' into a
'main' python file for personal use
"""

# Method 1
from PDFReader import readPDF, printPDF

pdf1 = readPDF('test_files/Test2PDF.pdf')
printPDF(pdf1)

# Method 2 
import PDFReader

pdf2 = PDFReader.readPDF('test_files/Test3PDF.pdf')
PDFReader.printPDF(pdf2)
