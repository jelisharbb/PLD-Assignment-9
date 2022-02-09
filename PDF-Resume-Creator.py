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
pdf.set_margin(12.7)

def headerDetails(header):
    header.image('resume picture.jpg', 155, 10, 50.8)
    header.set_font('helvetica', 'B', 30)
    header.cell(110, 15, "Jelisha Ruth Bugnon", ln=True, align='c')
    header.set_font('helvetica', '', 20)
    header.cell(90, 10, "Junior Software Developer", ln=True, align='c')
    header.ln(25)

def personalDetails(personal):
    personal.set_font('helvetica', 'B', 20)
    personal.cell(90, 10, "Personal Information", ln=1, align='c')
    personal.ln(3)
    personal.set_font('helvetica', '', 12)
    personal.cell(40, 6, "Name: " + str(resumeData["Personal Information"][0]["Name"]), ln=10)
    personal.cell(40, 6, "Sex: " + str(resumeData["Personal Information"][0]["Sex"]), ln=10)
    personal.cell(40, 6, "Age: " + str(resumeData["Personal Information"][0]["Age"]), ln=10)
    personal.cell(40, 6, "Address: " + str(resumeData["Personal Information"][0]["Address"]), ln=10)
    personal.cell(40, 6, "Contact Number: " + str(resumeData["Personal Information"][0]["Contact Number"]), ln=10)
    personal.cell(40, 6, "Email: " + str(resumeData["Personal Information"][0]["Email Address"]), ln=10)
    personal.ln(3)

def summaryDetails(summary):
    summary.set_font('helvetica', 'B', 20)
    summary.cell(90, 10, "Summary", ln=1, align='c')
    summary.ln(3)
    summary.set_font('helvetica', '', 12)
    summary.cell(40, 6, '' + str(resumeData["Summary"][0]), ln=10)
    summary.ln(3)

def experienceDetails(exp):
    exp.set_font('helvetica', 'B', 20)
    exp.cell(90, 10, "Experience", ln=1, align='c')
    exp.ln(3)
    exp.set_font('helvetica', '', 12)
    exp.cell(40, 6, '' + str(resumeData["Experience"][0]["Former Work"]), ln=10)
    exp.cell(40, 6, '' + str(resumeData["Experience"][0]["Former Company"]), ln=10)
    exp.cell(40, 6, '' + str(resumeData["Experience"][0]["Former Description"]), ln=10)
    exp.cell(40, 6, '' + str(resumeData["Experience"][0]["Latter Work"]), ln=10)
    exp.cell(40, 6, '' + str(resumeData["Experience"][0]["Latter Company"]), ln=10)
    exp.cell(40, 6, '' + str(resumeData["Experience"][0]["Latter Description"]), ln=10)
    exp.ln(3)

def educationDetails(educ):
    educ.set_font('helvetica', 'B', 20)
    educ.cell(90, 10, "Education", ln=1, align='c')
    educ.ln(3)
    educ.set_font('helvetica', '', 12)
    educ.cell(40, 6, '' + str(resumeData["Education"][0]["Course"]), ln=10)
    educ.cell(40, 6, '' + str(resumeData["Education"][0]["University"]), ln=10)
    educ.cell(40, 6, '' + str(resumeData["Education"][0]["Address"]), ln=10)
    educ.ln(3)

def projectDetails(proj):
    proj.set_font('helvetica', 'B', 20)
    proj.cell(90, 10, "Projects", ln=1, align='c')
    proj.ln(3)
    proj.set_font('helvetica', '', 12)
    proj.cell(40, 6, '' + str(resumeData["Projects"][0]["Project"]), ln=10)
    proj.cell(40, 6, '' + str(resumeData["Projects"][0]["Position"]), ln=10)
    proj.cell(40, 6, '' + str(resumeData["Projects"][0]["Description"]), ln=10)
    proj.ln(3)

def skillsDetails(skill):
    skill.set_font('helvetica', 'B', 20)
    skill.cell(90, 10, "Skills", ln=1, align='c')
    skill.ln(3)
    skill.set_font('helvetica', '', 12)
    skill.cell(40, 6, '' + str(resumeData["Skills"][0]), ln=10)
    skill.cell(40, 6, '' + str(resumeData["Skills"][1]), ln=10)
    skill.cell(40, 6, '' + str(resumeData["Skills"][2]), ln=10)
    skill.cell(40, 6, '' + str(resumeData["Skills"][3]), ln=10)
    skill.cell(40, 6, '' + str(resumeData["Skills"][4]), ln=10)
    skill.ln(3)

headerDetails(pdf)
personalDetails(pdf)
summaryDetails(pdf)
experienceDetails(pdf)
projectDetails(pdf)
skillsDetails(pdf)

# making pdf
pdf.output('BUGNON_JELISHARUTH.pdf')