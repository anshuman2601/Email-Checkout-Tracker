import PyPDF2
import time

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

dates = text[index+1:index+10]
print ('Book Due On: ' + dates)

hours = text[index+11:index+16]
print ('Due Time: ' + hours)

dates1 = int(dates[5:9])
dates2 = int(dates[0:1])
dates3 = int(dates[2:4])


#print('In how many days do you need a reminder?')
#local_time = float(input())
#Converting Days to seconds for the sleep method to work.
#local_time = local_time*60*60*24

#time.sleep(local_time)
#print ('Book Due On: ' + dates)
#print ('Due Time: ' + hours)
