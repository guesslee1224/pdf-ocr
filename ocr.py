import ocrmypdf
import pytesseract
import os
import sys

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

source_path = filedialog.askdirectory()
destination_path = filedialog.askdirectory()


def ocr(source, target):

    for filename in os.listdir(source):
        if (filename.endswith(".pdf")):
            source_pdf = (source + '/' + filename)
            clean_pdf_name = os.path.splitext(filename)[0]
            ocrmypdf.ocr(source_pdf, destination_path + '/' +
                         clean_pdf_name + '.pdf',  skip_text=True)


ocr(source_path, destination_path)

print('All done!')

# may have to switch slashes on Windows computer
# required pip3 Homebrew / ocrmypdf / pytesseract/ ghostscript
