# Pede ao utilizador um número N (entre 1 e 10) 
# e imprime uma pirâmide de altura N, como esta:
# Se N = 4, imprime:
   #  
  ##  
 ###  
####

print("Exercicio 1: Pirâmide")
# Saída:icio 1: Pirâmide de niveis")
x = int(input("Insira um número: "))
y = x 

for i in range(1, x + 1):
    y -= 1
    print(" " * y + "#" * i)


# Pede ao utilizador um número inteiro positivo e imprime-o ao contrário.

# Exemplo
# Entrada: 12345 54321

print("Exercicio 2: Número Reverso")

# Pedir um número inteiro positivo
num = int(input("Insira um número: "))

# Inicializa a variável para o número invertido
num_reverso = 0

# Enquanto o número for maior que 0
while num > 0:
    # Pega o último dígito do número
    digito = num % 10
    
    # Adiciona esse dígito ao número invertido
    num_reverso = num_reverso * 10 + digito
    
    # Remove o último dígito do número original
    num = num // 10

# Imprimir o número invertido
print("Número invertido:", num_reverso)