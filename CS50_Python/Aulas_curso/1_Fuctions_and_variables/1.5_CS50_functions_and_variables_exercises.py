#Exercicio 1
#Cria uma função chamada repetir_palavra que recebe duas coisas:

#Uma palavra
#Um número n

#A função deve retornar a palavra repetida n vezes.

print("Execicio 1:")    
def repetir_palavra(palavra, n):
    return palavra * n

numero = int(input("Quantas vezes vai querer repetir a palavra? "))
print(repetir_palavra("Python", numero))



#Exercicio 2
# Cria uma função chamada minutos_para_segundos que recebe um número 
# de minutos e retorna quantos segundos isso representa.

print("Execicio 2:")
def minutos_para_segundos(minutos):
    return minutos * 60

tempo = int(input("Quantos minutos? "))
print(minutos_para_segundos(tempo))

#Exercicio 3
# Cria uma função chamada soma que recebe dois números e retorna a soma deles.
# Depois, pede ao utilizador para inserir dois números e mostra o resultado

print("Execicio 3:")
def soma(n,y):
    return n + y

num1 = int(input("Qual é o seu primeiro número? "))
num2 = int(input("Qual é o seu segundo número? "))

print("O resultado da soma dos dois numéros é", soma(num1,num2))


#Exercicio 4
# Cria uma função chamada media que recebe três números e retorna a média deles.
# Depois, pede ao utilizador para inserir três números e imprime o resultado.

print("Execicio 4:")
def media(n1,n2,n3):
    return (n1+n2+n3)/3

a = int(input("Qual é o seu primeiro número? "))
b = int(input("Qual é o seu segundo número? "))
c = int(input("Qual é o seu terceiro número? "))

print("A média destes três números é", media(a,b,c))


#Exercicio 5
# Cria uma função chamada saudacao que recebe um nome e retorna uma mensagem de boas-vindas.
# Depois, pede ao utilizador para inserir o nome e mostra a saudação.

print("Execicio 5:")
def saudacao(nome):
    return "Olá, " + nome

nome1 = (input("Como se chama? "))

print(saudacao(nome1))


#Exercicio 6
# Cria uma função chamada mensagem que recebe duas variáveis: um nome e uma cidade.
# Depois, imprime uma mensagem do tipo:
# "Olá [nome]! Espero que estejas a gostar de [cidade]!"

print("Execicio 6:")
def mensagem(nome, cidade):
    return "Olá " + nome + "! Espero que estejas a gostar de " + cidade

nome2 = input("Como se chama? ")
cidade1 = input("Em que cidade está? ")

print(mensagem(nome2,cidade1))