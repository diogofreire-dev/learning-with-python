# Desenvolve uma função que recebe uma lista e um índice fornecido pelo utilizador.
# Tenta exibir o elemento na posição indicada e 
# trata a exceção caso o índice esteja fora dos limites da lista.

def acessar_elemento(lista):
    while True:
        try:
            indice = int(input("Insere o índice do elemento que desejas aceder: "))
            elemento = lista[indice]
            print(f"O elemento no índice {indice} é: {elemento}")
            break
        except IndexError:
            print("Erro: Índice fora do intervalo da lista. Tente novamente.")
        except ValueError:
            print("Erro: Por favor, insere um número inteiro válido.")

minha_lista = [10, 20, 30, 40, 50]
acessar_elemento(minha_lista)
