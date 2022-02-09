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

# open JSON file to python
with open("resume.json", "r") as resumeJson:
    resumeData = json.loads(resumeJson.read())

# set PDF format
pdf = FPDF('P', 'mm', 'Letter')
pdf.add_page()
pdf.set_margin(12.7)

# display header
def headerDetails(header):
    header.image('resume picture.jpg', 152, 10, 50.8)
    header.set_font('helvetica', 'B', 27)
    header.cell(115, 10, "Jelisha Ruth Bugnon", ln=True, align='L')
    header.set_font('helvetica', '', 15)
    header.cell(100, 10, "JUNIOR SOFTWARE DEVELOPER", ln=True, align='L')
    header.ln(8)

# display personal information data
def personalDetails(personal):
    personal.set_font('helvetica', 'B', 15)
    personal.set_fill_color(224, 224, 224)
    personal.cell(135, 8, "Personal Information", fill=True, ln=1, align='L')
    personal.ln(1)
    personal.set_font('helvetica', '', 11)
    personal.cell(40, 6, "Name                   : " + str(resumeData["Personal Information"][0]["Name"]), ln=1)
    personal.cell(40, 6, "Sex                      : " + str(resumeData["Personal Information"][0]["Sex"]), ln=1)
    personal.cell(40, 6, "Age                      : " + str(resumeData["Personal Information"][0]["Age"]), ln=1)
    personal.cell(40, 6, "Address               : " + str(resumeData["Personal Information"][0]["Address"]), ln=1)
    personal.cell(40, 6, "Contact Number  : " + str(resumeData["Personal Information"][0]["Contact Number"]), ln=1)
    personal.cell(40, 6, "Email                   : " + str(resumeData["Personal Information"][0]["Email Address"]), ln=1)
    personal.ln(4)

# display summary
def summaryDetails(summary):
    summary.set_font('helvetica', 'B', 15)
    summary.set_fill_color(224, 224, 224)
    summary.cell(0, 8, "Summary", fill=True, ln=1, align='L')
    summary.ln(1)
    summary.set_font('helvetica', '', 11)
    summary.cell(40, 6, '' + str(resumeData["Summary"][0]), ln=1)
    summary.cell(40, 6, '' + str(resumeData["Summary"][1]), ln=1)
    summary.ln(4)

# display experience data
def experienceDetails(exp):
    exp.set_font('helvetica', 'B', 15)
    exp.set_fill_color(224, 224, 224)
    exp.cell(0, 8, "Experience", fill=True, ln=1, align='L')
    exp.ln(1)
    exp.set_font('helvetica', 'B', 11)
    exp.cell(40, 6, '' + str(resumeData["Experience"][0]["Former Work"]), ln=1)
    exp.set_text_color(96, 96, 96)
    exp.set_font('helvetica', 'BI', 11)
    exp.cell(40, 6, '' + str(resumeData["Experience"][0]["Former Company"]), ln=1)
    exp.set_text_color(0, 0, 0)
    exp.set_font('helvetica', '', 11)
    exp.cell(40, 6, '' + str(resumeData["Experience"][0]["Former Description"][0]), ln=1)
    exp.cell(40, 6, '' + str(resumeData["Experience"][0]["Former Description"][1]), ln=1)
    exp.ln(1)
    exp.set_font('helvetica', 'B', 11)
    exp.cell(40, 6, '' + str(resumeData["Experience"][0]["Latter Work"]), ln=1)
    exp.set_text_color(96, 96, 96)
    exp.set_font('helvetica', 'BI', 11)
    exp.cell(40, 6, '' + str(resumeData["Experience"][0]["Latter Company"]), ln=1)
    exp.set_text_color(0, 0, 0)
    exp.set_font('helvetica', '', 11)
    exp.cell(40, 6, '' + str(resumeData["Experience"][0]["Latter Description"]), ln=1)
    exp.ln(4)

# display education data
def educationDetails(educ):
    educ.set_font('helvetica', 'B', 15)
    educ.set_fill_color(224, 224, 224)
    educ.cell(0, 8, "Education", fill=True, ln=1, align='L')
    educ.ln(1)
    educ.set_font('helvetica', 'B', 11)
    educ.cell(40, 6, '' + str(resumeData["Education"][0]["Course"]), ln=1)
    educ.set_text_color(96, 96, 96)
    educ.set_font('helvetica', 'BI', 11)
    educ.cell(40, 6, '' + str(resumeData["Education"][0]["University"]), ln=1)
    educ.set_text_color(0, 0, 0)
    educ.set_font('helvetica', '', 11)
    educ.cell(40, 6, '' + str(resumeData["Education"][0]["Address"]), ln=1)
    educ.ln(4)

# display project data
def projectDetails(proj):
    proj.set_font('helvetica', 'B', 15)
    proj.set_fill_color(224, 224, 224)
    proj.cell(0, 8, "Projects", fill=True, ln=1, align='L')
    proj.ln(1)
    proj.set_font('helvetica', 'B', 11)
    proj.cell(40, 6, '' + str(resumeData["Projects"][0]["Project"]), ln=1)
    proj.set_text_color(96, 96, 96)
    proj.set_font('helvetica', 'BI', 11)
    proj.cell(40, 6, '' + str(resumeData["Projects"][0]["Position"]), ln=1)
    proj.set_text_color(0, 0, 0)
    proj.set_font('helvetica', '', 11)
    proj.cell(40, 6, '' + str(resumeData["Projects"][0]["Description"]), ln=1)
    proj.ln(4)

# display skills data
def skillsDetails(skill):
    skill.set_font('helvetica', 'B', 15)
    skill.set_fill_color(224, 224, 224)
    skill.cell(0, 8, "Skills", fill=True, ln=1, align='L')
    skill.ln(1)
    skill.set_font('helvetica', '', 11)
    skill.cell(40, 6, '' + str(resumeData["Skills"][0]), ln=1)
    skill.cell(40, 6, '' + str(resumeData["Skills"][1]), ln=1)
    skill.cell(40, 6, '' + str(resumeData["Skills"][2]), ln=1)
    skill.cell(40, 6, '' + str(resumeData["Skills"][3]), ln=1)
    skill.cell(40, 6, '' + str(resumeData["Skills"][4]), ln=1)
    skill.ln(2)

# display note
def noteDetails(note):
    note.set_font('helvetica', 'I', 9)
    note.cell(40, 6, 'Note: ' + str(resumeData["Note"][0]), ln=1)

# calling out all the defined functions 
headerDetails(pdf)
personalDetails(pdf)
summaryDetails(pdf)
experienceDetails(pdf)
educationDetails(pdf)
projectDetails(pdf)
skillsDetails(pdf)
noteDetails(pdf)

# making pdf
pdf.output('BUGNON_JELISHARUTH.pdf')