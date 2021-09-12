from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
from PIL import Image, ImageDraw, ImageFilter, ImageOps
from tkinter import *
from tkinter import filedialog
import os
import PIL.Image

window = Tk()
window.title('File Explorer')
window.geometry("500x500")
window.config(background = "white")

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.pdf*"),
                                                       ("all files",
                                                        "*.*")))
    label_file_explorer.configure(text="File Opened: "+filename)
    # print(filename)
    path = os.path.dirname(filename)
    images = convert_from_path(filename,poppler_path=r'C:\Program Files\poppler-0.68.0\bin')
    images[0].save('pdfToImage.jpg', 'JPEG')
    im = PIL.Image.open(r"pdfToImage.jpg")
    im1 = im.crop((0, 340, 7300, 4800))
    im1.save("frontSide.jpg", 'JPEG')
    picture = im.crop((5150, 2150, 5730, 2830))
    picture.save("picture.jpg", 'JPEG')
    frontSide = PIL.Image.open('frontSide.jpg')
    picture = PIL.Image.open('picture.jpg')
    pictureSizeIncress = picture.resize((1350, 1350))
    frontSide.paste(pictureSizeIncress,(5700, 430))
    frontSide.save("pictureImplementinLarge.jpg", 'JPEG')
    yellowBox = im.crop((5150, 1500, 5730, 2000))
    yellowBox.save("yellowBox.jpg", 'JPEG')
    yellowBoxSizeIncress = yellowBox.resize((650, 750))
    frontSide.paste(yellowBoxSizeIncress,(5080, 1800))
    frontSide.save("finalFrontSideremovePic.jpg", 'JPEG')
    issueDateAndCertificate = im.crop((7360, 300, 9520, 1600))
    issueDateAndCertificate.save("issueDateAndCertificate.jpg", 'JPEG')
    qrCode = im.crop((7690, 3940, 9060, 5650))
    qrCode.save("qrCode.jpg", 'JPEG')
    backSide = PIL.Image.open('backSide.jpg')
    picture = PIL.Image.open('picture.jpg')
    pictureSizeIncress = picture.resize((1500, 1500))
    backSide.paste(pictureSizeIncress,(300, 300))
    backSide.save("backSideNew.jpg", 'JPEG')
    # if vac == 1:
    # fullyVaccinated = PIL.Image.open('fullyVaccinated.jpg')
    # pictureSizeIncress = fullyVaccinated.resize((700, 700))
    # backSide.paste(pictureSizeIncress,(2050, 320))
    # backSide.save("backSideNew.jpg", 'JPEG')
    logo = PIL.Image.open('logo.jpg')
    logoSizeIncress = logo.resize((1500, 1500))
    backSide.paste(logoSizeIncress,(5400, 280))
    backSide.save("backSideNew.jpg", 'JPEG')
    issueDateAndCertificate = PIL.Image.open('issueDateAndCertificate.jpg')
    # issueDateAndCertificateSizeIncress = issueDateAndCertificate.resize((1500, 1500))
    backSide.paste(issueDateAndCertificate,(2950, 1300))
    backSide.save("backSideNew.jpg", 'JPEG')
    qrCode = PIL.Image.open('qrCode.jpg')
    # pictureSizeIncress = picture.resize((1500, 1500))
    backSide.paste(qrCode,(300, 2600))
    backSide.save("backSideNew.jpg", 'JPEG')
    signature = PIL.Image.open('signature.jpg')
    signatureSizeIncress = signature.resize((2800, 1500))
    backSide.paste(signatureSizeIncress,(4200, 2800))
    backSide.save("backSideNew.jpg", 'JPEG')
    a4 = PIL.Image.open('a4.jpg')
    finalBackSide = PIL.Image.open('backSideNew.jpg')
    width, height = finalBackSide.size
    width = int(width/3.4)
    height = int(height/3.4)
    # print(width)
    # print(height)
    finalBackSideChangedSize = finalBackSide.resize((width,height))
    a4.paste(finalBackSideChangedSize,(500,500))
    a4.save("Back.jpg", 'JPEG')
    
    finalFrontSide = PIL.Image.open('finalFrontSideremovePic.jpg')
    
    
    a4back = PIL.Image.open('a4.jpg')
    width, height = finalFrontSide.size
    width = int(width/3.4)
    height = int(height/3.4)
    # print(width)
    # print(height)
    finalFrontSideChangedSize = finalFrontSide.resize((width,height))
    a4back.paste(finalFrontSideChangedSize,(500,500))
    a4back.save("Front.jpg", 'JPEG')
	



label_file_explorer = Label(window,
                            text = "File Explorer using Tkinter",
                            width = 100, height = 4,
                            fg = "blue")
  
      
button_explore = Button(window,
                        text = "Browse Files",
                        command = browseFiles)
  
button_exit = Button(window,
                     text = "Exit",
                     command = exit)

label_file_explorer.grid(column = 1, row = 1)
button_explore.grid(column = 1, row = 2)
button_exit.grid(column = 1,row = 3)
window.mainloop()