from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 48)
        title = "CS50 Shirtificate"
        title_width = self.get_string_width(title)
        # Centraliza o título horizontalmente
        self.set_x((210 - title_width) / 2)
        # Adiciona o título
        self.cell(title_width, 60, title, 0, 1, 'C')
        self.ln(10)


def main():
    # Pede o nome ao utilizador
    name = input("Name: ")
    
    # Cria o PDF
    pdf = PDF()
    pdf.add_page()
    
    # Adiciona a imagem da t-shirt (centralizada)
    # A4 tem 210mm de largura, imagem com 190mm fica centralizada
    pdf.image("shirtificate.png", x=10, y=70, w=190)
    
    # Adiciona o nome com "took CS50" sobre a t-shirt
    # Define posição Y (aproximadamente no meio da t-shirt)
    pdf.set_y(140)
    # Define fonte branca e tamanho
    pdf.set_font('Arial', 'B', 24)
    pdf.set_text_color(255, 255, 255)  # Branco
    # Cria o texto completo: "NOME took CS50"
    shirt_text = f"{name} took CS50"
    # Centraliza o texto horizontalmente
    pdf.cell(0, 10, shirt_text, 0, 1, 'C')
    
    # Guarda o PDF
    pdf.output(f"shirtificate_{name.replace(" ","-")}.pdf")
    print("Shirtificate created successfully!")


if __name__ == "__main__":
    main()