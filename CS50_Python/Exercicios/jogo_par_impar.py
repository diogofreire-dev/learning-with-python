import random

# O usuário joga contra o computador escolhendo par ou ímpar
# O usuário e computador escolhem um número aleatório entre 1 e 10
# O usuário ganha se o resultado da soma for par ou ímpar de acordo com a sua escolha 
def par_ou_impar():
    escolha = input("Escolha Par (P) ou Ímpar (I): ").strip().upper()
    num_usuario = int(input("Digite um número: "))
    num_computador = random.randint(1, 10)
    
    soma = num_usuario + num_computador
    resultado = "P" if soma % 2 == 0 else "I"

    print(f"A tua escolha foi {num_usuario}, o computador escolheu {num_computador}.")
    print(f"A soma é {soma}, que é {'Par' if resultado == 'P' else 'Ímpar'}.")

    if escolha == resultado:
        print("Parabéns! Você ganhou!")
    else:
        print("O computador venceu!")

par_ou_impar()
