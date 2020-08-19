from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter #similarly HTMLConverter , XMLConverter
from pdfminer.layout import LAParams
import io

#open the pdf file
pdf=open('F:\\Education\\Alien Brains\\Selections.pdf','rb')

#generate the interpreter
mem=io.StringIO()
rm=PDFResourceManager()
lp=LAParams()
cnv=TextConverter(rm,mem,laparams=lp)
interpreter=PDFPageInterpreter(rm,cnv)

#for each page of the file
for i in PDFPage.get_pages(pdf):
	#interpret the text
	interpreter.process_page(i)
	#save it
	text = mem.getvalue()

file=open('F:\\Education\\Alien Brains\\pdf.txt','wb')
file.write(text.encode('utf-8'))
print('DONE')


