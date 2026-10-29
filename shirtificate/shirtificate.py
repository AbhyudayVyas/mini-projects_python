from fpdf import FPDF, Align

def main():
    name = input('Enter your name: ')
    pdf = FPDF(orientation='P', format='A4')
    pdf.add_page()
    pdf.set_font("helvetica", style="B", size=25)
    pdf.cell(w=0, h=10, text="CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.image("shirtificate.png", x=Align.C, y=25)
    pdf.set_xy(0, 10)
    pdf.set_text_color(255,255,255)
    pdf.cell(w=215, h=175, text=name+" took CS50", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.output("shirtificate.pdf")

if __name__ == '__main__':
    main()