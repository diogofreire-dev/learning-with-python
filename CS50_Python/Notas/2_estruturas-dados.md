# Estruturas de Dados em Python

## Listas Avançadas

```python
números = [1, 2, 3, 4, 5]

# Operações úteis
números.insert(0, 0)      # Inserir 0 na posição 0
números.extend([6, 7])    # Adicionar vários elementos
último = números.pop()    # Remove e devolve o último (7)
números.sort()            # Ordena a lista [0,1,2,3,4,5,6]
números.reverse()         # Inverte a lista [6,5,4,3,2,1,0]

# Cortar listas (slicing)
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
primeiros_três = lista[0:3]  # [0, 1, 2]
últimos_dois = lista[-2:]    # [8, 9]
pares = lista[::2]           # [0, 2, 4, 6, 8]
invertida = lista[::-1]      # [9, 8, 7, ... 0]

# Compreensão de lista (list comprehension)
quadrados = [x**2 for x in range(10)]
pares = [x for x in range(20) if x % 2 == 0]
```

## Tuplos (Tuples)

São como listas, mas não podem ser alterados depois de criados.

```python
# Criar tuplos
coordenadas = (10, 20)
pessoa = ("João", 25, "Professor")

# Desempacotar (unpack)
x, y = coordenadas         # x=10, y=20
nome, idade, prof = pessoa  # Separar em variáveis

# Não podemos alterar tuplos
# coordenadas[0] = 15  # Isto dá erro!
```

## Conjuntos (Sets)

Coleções sem elementos repetidos e sem ordem definida.

```python
# Criar conjuntos
frutas = {"maçã", "banana", "laranja"}
números = set([1, 2, 2, 3, 3, 4])  # {1, 2, 3, 4}

# Operações
frutas.add("uva")          # Adicionar elemento
frutas.remove("banana")    # Remover elemento

# Operações matemáticas
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
união = a | b              # {1, 2, 3, 4, 5, 6}
interseção = a & b         # {3, 4}
diferença = a - b          # {1, 2}
```

## Dicionários Avançados

```python
aluno = {
    "nome": "Pedro",
    "notas": [16, 18, 15],
    "curso": "Informática"
}

# Aceder de forma segura (sem erros)
curso = aluno.get("curso", "Desconhecido")
morada = aluno.get("morada", "Não definida")

# Iterar pelo dicionário
for chave in aluno:
    print(f"Chave: {chave}, Valor: {aluno[chave]}")

for chave, valor in aluno.items():
    print(f"{chave}: {valor}")

# Verificar se existe
if "nome" in aluno:
    print("Nome está definido!")

# Compreensão de dicionário
quadrados = {x: x**2 for x in range(5)}  # {0:0, 1:1, 2:4, 3:9, 4:16}
```
