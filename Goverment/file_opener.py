import PyPDF2
import docx
from reportlab.pdfgen import canvas

def read_pdf(pdf_file):
    text = ""
    with open(pdf_file, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def read_docx(docx_file):
    doc = docx.Document(docx_file)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + '\n'
    return text


def create_pdf(file_path, text):
    c = canvas.Canvas(file_path)
    c.drawString(100, 750, text)
    c.showPage()
    c.save()

def create_txt(file_path, text):
    with open(file_path, 'w') as file:
        file.write(text)



