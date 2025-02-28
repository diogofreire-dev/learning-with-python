# Escreve uma função que peça ao utilizador para inserir dois números e, 
# em seguida, exiba o resultado da divisão do primeiro pelo segundo. 
# Garante que o programa trata 
# a exceção de divisão por zero.
def divisao():
    while True:
        try:
            x = int(input("Insira um número: "))
            y = int(input("Insira outro número: "))
            result = x / y      
            print(f"O resultado da divisão é: {result}")
        except ValueError:
            print("Por favor, insira números válidos.")
        except ZeroDivisionError:
            print("Não é possível dividir por zero. Por favor, insira outro número.")

divisao()