from fpdf import FPDF

class CertificatePDF(FPDF):
    def header(self):
        self.image("./shirtificate.png", 10, 70, 190)
        self.set_font("helvetica", "", 48)
        self.cell(0, 57, "CS50 Achievement", align="C")
        self.ln(20)


def main():
    user_name = input("Enter your name: ")
    create_certificate(user_name)


def create_certificate(name):
    pdf = CertificatePDF()
    pdf.add_page(orientation="portrait", format="a4")
    pdf.set_font("helvetica", size=24)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 213, f"{name} completed CS50", align="C")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
