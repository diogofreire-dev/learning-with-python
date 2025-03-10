# Funções e Algoritmos em Python

## Funções Avançadas

```python
# Documentação de funções
def calcular_média(números):
    """
    Calcula a média aritmética de uma lista de números.
    
    Args:
        números: Uma lista ou tuplo com números
        
    Returns:
        A média dos números ou 0 se a lista estiver vazia
    """
    if not números:
        return 0
    return sum(números) / len(números)

# Múltiplos argumentos (args)
def soma(*números):
    """Soma todos os números fornecidos."""
    total = 0
    for n in números:
        total += n
    return total

# Usar a função com qualquer quantidade de argumentos
soma(1, 2)           # 3
soma(1, 2, 3, 4, 5)  # 15

# Argumentos nomeados (kwargs)
def criar_perfil(nome, **detalhes):
    """Cria um perfil com nome e detalhes variáveis."""
    perfil = {"nome": nome}
    perfil.update(detalhes)
    return perfil

# Usar com argumentos nomeados variáveis
perfil1 = criar_perfil("Ana", idade=25, cidade="Porto")
perfil2 = criar_perfil("João", idade=30, profissão="Médico", casado=True)
```

## Funções Lambda (Anónimas)

```python
# Função lambda simples
dobro = lambda x: x * 2

# Usar a função lambda
dobro(5)  # 10

# Útil com funções como map, filter e sort
números = [1, 5, 2, 8, 3]
quadrados = list(map(lambda x: x**2, números))  # [1, 25, 4, 64, 9]
pares = list(filter(lambda x: x % 2 == 0, números))  # [2, 8]

# Ordenar uma lista de tuplos
alunos = [("Ana", 18), ("João", 16), ("Pedro", 19)]
# Ordenar por nota (segundo elemento)
alunos_ordenados = sorted(alunos, key=lambda aluno: aluno[1])
```

## Algoritmos Básicos

```python
# Procura linear (em lista não ordenada)
def procura_linear(lista, alvo):
    for i, valor in enumerate(lista):
        if valor == alvo:
            return i  # devolve o índice
    return -1  # não encontrado

# Procura binária (em lista ordenada)
def procura_binária(lista, alvo):
    esquerda, direita = 0, len(lista) - 1
    
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
            
    return -1  # não encontrado

# Ordenação - Bubble Sort
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista
```

## Recursividade

```python
# Função recursiva para calcular fatorial
def fatorial(n):
    if n <= 1:  # caso base
        return 1
    return n * fatorial(n - 1)  # chamada recursiva

# Sequência de Fibonacci recursiva
def fibonacci(n):
    if n <= 1:  # casos base
        return n
    return fibonacci(n-1) + fibonacci(n-2)  # chamada recursiva
```
