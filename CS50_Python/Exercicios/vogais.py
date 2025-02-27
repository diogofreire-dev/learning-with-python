# Conta quantas vogais existem em uma string

def contar_vogais():
    texto = input("Digite uma frase: ")
    vogais = "aeiouAEIOU"
    total_vogais = sum(1 for letra in texto if letra in vogais)

    print(f"A frase contém {total_vogais} vogais.")

contar_vogais()
