import fitz
import os

def pdf2text(filepath, save_img = None):
    '''
    A function that extracts all images and text from pdfs.
    Extracted images are stored in imagePath and text is returned.

    Requirements: pip install PyMuPDF

    Args: 
        fileName (string): Path to pdf file
        imagePath (string): Path where extracted images go
    '''
    #create temp image path if no path to save extracted images is provided
    if save_img == None:
        if not os.path.isdir('temp_images_dir'):
            os.mkdir('temp_images_dir')
        return pdf2text(filepath, 'temp_images_dir')
    
    pdf = fitz.open(filepath)
    #extract images
    for page_index in range(len(pdf)):
        for image_index, img in enumerate(pdf.get_page_images(page_index)):
            xref = img[0]       #get XREF of image
            pix = fitz.Pixmap(pdf, xref)
            if pix.n < 5:       #image is GRAY or RGB
                pix.save(f"{save_img}/Page%s-Image%s.png" % (page_index+1, image_index+1))
            else:               #CMYK: convert to RGB
                pix1 = fitz.Pixmap(fitz.csRGB, pix)
                pix1.save(f"{save_img}/Page%s-Image%s.png" % (page_index+1, image_index+1))
                pix1 = None

    #extract text
    text = ''
    with pdf as doc:
        for page in doc:
            text += page.get_text()
        return text