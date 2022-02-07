# PDF Resume Creator
# 	- Create a python program that will create your personal resume in PDF format
# 	- All personal details are stored in a JSON file
# 	- Your program should read the JSON file and write the details in the PDF
# 	- The output file should be: LASTNAME_FIRSTNAME.pdf

# Note:
# 	- Search for available PDF library that you can use
# 	- Search how data is structured using JSON format
# 	- Search how to read JSON file
# 	- You will create the JSON file manually
# 	- Your code should be in github before Feb12


""" PDF Resume Creator """

from fpdf import FPDF

# specify the layout (portrait), unit (millimeters), and format (letter size) of the pdf
pdf = FPDF ('P', 'mm', 'Letter')

# add a page
pdf.add_page() 

# specify font, regular/default (not bold, italic, or underlined), and font size
pdf.set_font('helvetica', '', 16)

# add text (width, height, text)
pdf.cell(40, 10, 'Hello, world!')

# generating pdf
pdf.output('BUGNON_JELISHARUTH.pdf')




