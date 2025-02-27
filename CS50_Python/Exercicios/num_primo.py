# Verifica se um número é primo ou não
def numero_primo():
    numero = int(input("Digite um número: "))
    if numero < 2:
        print("Não é primo.")
        return

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            print("Não é primo.")
            return

    print("É um número primo!")

numero_primo()
