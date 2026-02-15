from pdf2docx import Converter
pdf_file="sample.pdf"

doc_pdf="sample.doc"
cv=Converter(pdf_file)
cv.convert(doc_pdf)
cv.close()