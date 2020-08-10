from PyPDF2 import PdfFileWriter,PdfFileReader

#merge pdfs together

#create write object
write_obj = PdfFileWriter()
#make a list
pdf_list=["F:\\Education\\Alien Brains\\Playing_with_pdfs\\Recommendation_Systems.pdf","F:\\Education\\Alien Brains\\Playing_with_pdfs\\Machine_Learning.pdf"]
#read the pdfs and write in write_obj
for i in pdf_list:
	read_obj = PdfFileReader(i)
	pages = read_obj.getNumPages()
	for j in range(pages):
		p=read_obj.getPage(j)
		write_obj.addPage(p)

#encrypt pdf file
write_obj.encrypt("enemiesahead","jaiho",True)
#write object to pdf file
pdf_file = open("F:\\Education\\Alien Brains\\Playing_with_pdfs\\mergedpdf.pdf","wb")
write_obj.write(pdf_file)
pdf_file.close()

#add watermark
pdf = PdfFileReader("F:\\Education\\Alien Brains\\Playing_with_pdfs\\Recommendation_Systems.pdf")
watermark = PdfFileReader("F:\\Education\\Alien Brains\\Playing_with_pdfs\\pngfuel.pdf")
page_w = watermark.getPage(0)
new_pdf=PdfFileWriter()
pages=pdf.getNumPages() 
for i in range(pages):
	page = pdf.getPage(i)
	page.mergePage(page_w)
	new_pdf.addPage(page)

pdf_f = open("F:\\Education\\Alien Brains\\Playing_with_pdfs\\Watermarked.pdf","wb")
new_pdf.write(pdf_f)

pdf_f.close()