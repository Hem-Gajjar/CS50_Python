from fpdf import FPDF

class PDF():
    def __init__(self,name):
        self._pdf= FPDF()
        self._pdf.add_page()
        self._pdf.set_font("helvetica","8",50)
        self.pdf.cell(0, 60, 'CS% Shirtificate', new_x="LMARGIN", new_y="NEXT", align='C')
        self._pdf.image("shirtificate.png",w=self._pdf.epw)

    def save(self,name):
        self._pdf.output(name)



name = input("Name: ")
pdf = PDF(name)
pdf.save("shirtificate.pdf")
