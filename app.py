import PyPDF2

# read in binary mode
with open("directory/first.pdf", "rb") as file_stream:
    reader = PyPDF2.PdfFileReader(file_stream)
    print(reader.numPages)
    page = reader.getPage(0)
    page.rotateClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    # add this page object at the end of this new pdf in memory
    writer.addPage(page)
    # # add this page object at a specific index
    # writer.insertPage(page, 0)
    with open("directory/rotated.pdf", "wb") as output:
        writer.write(output)
