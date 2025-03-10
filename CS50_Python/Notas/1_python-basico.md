# Python Básico

## Variáveis e Tipos de Dados

Em Python, não precisamos declarar o tipo das variáveis.

```python
# Tipos básicos
nome = "João"    # string (texto)
idade = 25       # int (número inteiro)
altura = 1.75    # float (número decimal)
estudante = True # boolean (verdadeiro/falso)
```

## Operações Básicas

```python
# Matemática básica
soma = 10 + 5          # 15
subtração = 10 - 5     # 5
multiplicação = 10 * 5 # 50
divisão = 10 / 5       # 2.0 (sempre devolve float)
divisão_inteira = 10 // 3  # 3 (corta a parte decimal)
resto = 10 % 3         # 1 (resto da divisão)
potência = 2 ** 3      # 8 (2 elevado a 3)

# Comparações
igual = (5 == 5)       # True
diferente = (5 != 3)   # True
maior = (10 > 5)       # True
menor = (5 < 10)       # True
maior_igual = (5 >= 5) # True
menor_igual = (4 <= 5) # True
```

## Strings (Texto)

```python
# Juntar textos
nome = "João"
apelido = "Silva"
nome_completo = nome + " " + apelido  # "João Silva"

# Formatação
idade = 30
# f-strings (mais fácil de usar)
mensagem = f"Olá, chamo-me {nome} e tenho {idade} anos."

# Funções de texto
texto = "  Python é fantástico  "
texto_minúsculo = texto.lower()       # para minúsculas
texto_maiúsculo = texto.upper()       # para maiúsculas
texto_sem_espaços = texto.strip()     # remove espaços início/fim
substituir = texto.replace("fantástico", "incrível")
```

## Condições

```python
idade = 18

if idade < 18:
    print("És menor de idade")
elif idade == 18:
    print("Acabaste de atingir a maioridade")
else:
    print("És maior de idade")
```

## Ciclos (Loops)

```python
# Ciclo for
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

# Ciclo while
contador = 0
while contador < 5:
    print(contador)
    contador += 1  # aumenta o contador em 1
```

## Listas

```python
# Criar e usar listas
frutas = ["maçã", "banana", "laranja"]
frutas.append("morango")     # adiciona ao final
primeiro = frutas[0]         # "maçã" (primeiro elemento)
ultimo = frutas[-1]          # "morango" (último elemento)
frutas.remove("banana")      # remove elemento
tamanho = len(frutas)        # tamanho da lista (3)
```

## Dicionários

```python
# Pares de chave-valor
pessoa = {
    "nome": "Ana",
    "idade": 25,
    "cidade": "Lisboa"
}

nome = pessoa["nome"]       # aceder a um valor
pessoa["profissão"] = "Engenheira"  # adicionar novo par
```

## Funções

```python
# Definir uma função
def saudação(nome):
    return f"Olá, {nome}!"

# Usar a função
mensagem = saudação("Carlos")  # "Olá, Carlos!"

# Função com valor padrão
def potência(base, expoente=2):
    return base ** expoente

quadrado = potência(3)     # 9 (3²)
cubo = potência(3, 3)      # 27 (3³)
```
