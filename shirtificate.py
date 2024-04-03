from fpdf import FPDF

class PDF():
    def __init__(self,name):
        self._pdf= FPDF()
        self._pdf.add_page()
        self._pdf.set_font("helvetica","8",50)

name = input("Name: ")
pdf = PDF(name)
pdf.save("shirtificate.pdf")
