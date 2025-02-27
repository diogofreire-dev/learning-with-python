# Escreve um programa que peça ao utilizador para inserir três números.
# Compara os três números e imprime qual é o maior e qual é o menor.

# Entrada: Três números fornecidos pelo utilizador.
# Saída: O maior e o menor número.

print("Exercicio 1:")
num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))
num3 = int(input("Insira o terceiro número: "))

maior = num1
menor = num1

if num2 > maior:
    maior = num2

if num2 < menor:
    menor = num2

if num3 > maior:
    maior = num3

if num3 < menor:
    menor = num3

print("O maior número é", maior)
print("O menor número é", menor)

"""
maior = max(num1, num2, num3)
menor = min(num1, num2, num3)
print("O maior número é", maior)
print("O menor número é", menor)
"""


# Escreve um programa que peça a idade do utilizador 
# e verifique se ele tem idade suficiente para votar (18 anos ou mais).

# Entrada: Idade.
# Saída: "Pode votar" ou "Não pode votar."

print("Exercicio 2:")
idade = int(input("Qual é a sua idade: "))

if idade >= 18:
    print("Pode votar!")
else:
    print("Não pode votar...")

"""
if mes < 1 or mes > 12:
    print("Mês inválido!")
else:
    # Continuação do código...
"""

# Cria um programa que peça ao utilizador 
# para inserir um mês (de 1 a 12) e retorne o número de dias nesse mês. 
# Considera o ano bissexto para o mês de fevereiro.

# Entrada: Mês (como um número inteiro).
# Saída: Número de dias no mês correspondente.

print("Exercicio 3:")
mes = int(input("Insira o número de um mês: "))

match mes:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print("Tem 31 dias")
    case 2:
        print("Tem 29 dias")
    case 4 | 6 | 9 | 11:
        print("Tem 30 dias")



# Escreve um programa onde o utilizador escreve uma string
# e o programa verifica se a string contém 
# a palavra "Python". Imprime "Python encontrado" se a string 
# contiver essa palavra, ou "Python não encontrado" se não contiver.

print("Exercicio 4:")
texto = input("Insira uma frase ou palavra: ")

if "Python" in texto or "python" in texto:
    print("Python encontrado")
else:
    print("Python não encontrado")

"""
if "python" in texto.lower():
    print("Python encontrado")
else:
    print("Python não encontrado")
"""