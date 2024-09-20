from fpdf import FPDF

pdf = FPDF(orientation='P', unit='pt', format='A4')
pdf.add_page()

pdf.image('ts.jpg', w=102, h=126 )
pdf.set_font(family='Times', style='B', size=24)
pdf.cell(w=0, h=50, txt="Tomislav Sokac", align='C', ln=1)

pdf.set_font(family="Times", style='B', size=14)
pdf.cell(w=0, h=15, txt='Description', ln=1)

pdf.set_font(family="Times", size=12)
txt1 = '''
API Integration Engineer | IT Guru,
able to plan and lead full project life cycles including excellent presentation and communications skills.
'''
pdf.multi_cell(w=0, h=10, txt=txt1)

pdf.set_font(family="Times", style='B', size=14)
pdf.cell(w=100, h=50, txt="Achievements: ")

pdf.set_font(family="Times", size=12)
pdf.cell(w=100, h=50, txt="Code Institute, 2022")


pdf.output('output.pdf')
