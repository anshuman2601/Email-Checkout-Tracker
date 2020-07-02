import PyPDF2

pdfObj = open('library checkout receipt.pdf', 'rb')

pdfRead = PyPDF2.PdfFileReader(pdfObj)

# Page Object (fetches the page, in our case since the file only has 1 page, it's indexed at 0)
page = pdfRead.getPage(0)

# Extracting Text from PDF
text = (page.extractText())

# Close the Object
pdfObj.close()

#print (text)

if 'Due Date:' in text:
    print (True)
    pos = text.index('Due Date:')
    index = pos + len('Due Date:')
    #print (index)
else:
    print (False)

date = text[index+1:index+10]
print (date)

time = text[index+11:index+16]
print (time)