import argparse
from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def docx_to_pdf(docx_path, pdf_path):
    doc = Document(docx_path)

    c = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica", 12)

    y_position = height - 40

    for para in doc.paragraphs:
        if y_position <= 40:
            c.showPage()
            c.setFont("Helvetica", 12)
            y_position = height - 40

        c.drawString(40, y_position, para.text)
        y_position -= 14

    c.save()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert .docx to PDF")
    parser.add_argument("docx_file", help="Path to the input .docx file")
    parser.add_argument("pdf_file", help="Path to the output PDF file")
    args = parser.parse_args()

    docx_to_pdf(args.docx_file, args.pdf_file)
