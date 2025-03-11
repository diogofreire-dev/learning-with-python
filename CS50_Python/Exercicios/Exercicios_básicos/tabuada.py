# Mostra a tabuada de um número escolhido pelo usuário
def tabuada():
    numero = int(input("Digite um número para ver sua tabuada: "))
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

tabuada()
