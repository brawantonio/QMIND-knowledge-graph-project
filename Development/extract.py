import sys

try:
    import docx2txt
except:
    print('Error:\tdocx2txt library has not been installed.\n\tTry \'pip install docx2txt\'.')
    sys.exit(0)

def extractTextFromDocx(fileName, imagePath, isList = None):
    '''
    A function that extracts all images and text (excluding math equations) from docx files.
    Images are stored in file path. Returns extracted text as one string unless isList is True.

    Requirements: pip install docx2txt

    Args:
        fileName (string): Path to docx file
        imagePath (string): Path where extracted images go
        isList (bool): if True, returns extracted text as a list of strings
    '''
    text = docx2txt.process(fileName, imagePath)
    if isList is True:
        text = text.split()
    return text

def extractTextFromTxt(fileName, isList = None):
    '''
    A function that extracts all text from txt files.
    Returns extracted text as one string unless isList is True.

    Args:
        fileName (string): Path to txt file
        isList (bool): if True, returns extracted text as a list of strings
    '''
    with open(fileName) as f:
        text = f.read().replace('\n', ' ')
        if isList is True:
            text = text.split()
        return text
