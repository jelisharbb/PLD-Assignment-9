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

# import function to be used
from fpdf import FPDF
import json

importResume = "resume.json"
with open(importResume, "r") as resumeJson:
    resumeData = json.loads(resumeJson.read())

pdf = FPDF('P', 'mm', 'Letter')
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)

def headerDetails(header):
    header.image('resume picture.jpg', 155, 10, 50.8)
    header.set_font('helvetica', 'B', 30)
    header.cell(110, 15, "Jelisha Ruth Bugnon", ln=True, align='c')
    header.set_font('helvetica', '', 20)
    header.cell(90, 10, "Junior Software Developer", ln=True, align='c')
    header.ln(25)

def personalDetails(personal):
    personal.cell(90, 10, "Personal Information", ln=1, align='c')
    personal.ln(3)
    personal.set_font('helvetica', '', 12)
    personal.cell(40, 6, "Name: " + str(resumeData["Personal Information"][0]["Name"]), ln=10)
    personal.cell(40, 6, "Sex: " + str(resumeData["Personal Information"][0]["Sex"]), ln=10)
    personal.cell(40, 6, "Age: " + str(resumeData["Personal Information"][0]["Age"]), ln=10)
    personal.cell(40, 6, "Address: " + str(resumeData["Personal Information"][0]["Address"]), ln=10)
    personal.cell(40, 6, "Contact Number: " + str(resumeData["Personal Information"][0]["Contact Number"]), ln=10)
    personal.cell(40, 6, "Email: " + str(resumeData["Personal Information"][0]["Email Address"]), ln=10)

def summaryDetails(summary):
    summary.cell(90, 10, "Summary", ln=1, align='c')
    summary.ln(3)
    summary.set_font('helvetica', '', 12)

headerDetails(pdf)
personalDetails(pdf)

# producing pdf
pdf.output('BUGNON_JELISHARUTH.pdf')