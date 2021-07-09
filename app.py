import PyPDF2

# read in binary mode
with open("directory/first.pdf", "rb") as file_stream:
    reader = PyPDF2.PdfFileReader(file_stream)
    print(reader.numPages)
