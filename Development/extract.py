import sys

try:
    import docx2txt
except:
    print('Error:\tdocx2txt library has not been installed.\n\tTry \'pip install docx2txt\'.')
    sys.exit(0)

def extractTextFromDocx(fileName, imagePath):
    '''
    A function that extracts all images and text (excluding math equations) from docx files.

    Requirements: pip install docx2txt

    Args: Must be string type variables

    Text is stored in variable. Images are stored in file path.
    '''
    text = docx2txt.process(fileName, imagePath) #first parameter is file name and second is file path for extracted images
