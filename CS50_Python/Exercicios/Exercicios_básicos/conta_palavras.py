# Conta quantas palavras existem em uma frase

def contar_palavras():
    frase = input("Digite uma frase: ").strip() # strip() remove espaços extras no inicio e no fim da string.
    palavras = frase.split() # split() divide a string em uma lista de palavras.
    print(f"A frase contém {len(palavras)} palavras.")

contar_palavras()
