import fitz

def extractPDFImages(fileName, imagePath=None):
    '''
    A function that extracts all images from pdfs.
    Extracted images are stored in imagePath.

    Requirements: pip install PyMuPDF

    Args: 
        fileName (string): Path to pdf file
        imagePath (string): Path where extracted images go
    '''
    pdf = fitz.open(fileName)
    for pageIndex in range(len(pdf)):
        for imageIndex, img in enumerate(pdf.get_page_images(pageIndex)):
            xref = img[0]       #get XREF of image
            pix = fitz.Pixmap(pdf, xref)
            if pix.n < 5:       #image is GRAY or RGB
                pix.save(f"{imagePath}/Page%s-Image%s.png" % (pageIndex+1, imageIndex+1))
            else:               #CMYK: convert to RGB
                pix1 = fitz.Pixmap(fitz.csRGB, pix)
                pix1.save(f"{imagePath}/Page%s-Image%s.png" % (pageIndex+1, imageIndex+1))
                pix1 = None