import PyPDF2

pdfFileObj = open('/home/rlnd/Downloads/Evaluating Energy Efficiency and Security for Internet of Things A Systematic Review.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

print(pdfReader.numPages)

pageObj = pdfReader.getPage(0)

print(pageObj.extractText())

pdfFileObj.close()