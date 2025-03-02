# Escreve um programa que peça ao utilizador 
# para inserir um número e, em seguida, 
# utilize a função sqrt da biblioteca math para 
# calcular e exibir a raiz quadrada desse número.

from math import sqrt

x = int(input("Insira um número: "))
print(f"A raiz quadrada de {x} é de {sqrt(x)}")