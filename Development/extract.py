import docx2txt

def extractTextFromDocx():
    '''
    Requirements: pip install docx2txt
    This function extracts text (excluding math equations) and images from docx files.
    Text is stored in variable. Images are stored in file path (second parameter of process() function). 
    '''
    text = docx2txt.process("Team-150-Assessment12T.docx", "img") #second parameter is file path where images 
    print(text)

extractTextFromDocx()