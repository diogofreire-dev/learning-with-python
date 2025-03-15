# Python Regular Expressions

## O que são Regular Expressions

Regular Expressions (RegEx) são padrões usados para encontrar combinações de caracteres em strings.

```python
# Importar o módulo de regex
import re
```

## Funções Básicas

```python
# Funções principais
re.search()    # Procura um padrão na string
re.match()     # Verifica se a string começa com o padrão
re.findall()   # Encontra todas as ocorrências do padrão
re.sub()       # Substitui ocorrências por outra string
```

## Procurar Padrões

```python
import re

texto = "O meu email é exemplo@email.com"

# Procurar um padrão na string
resultado = re.search(r"exemplo@email\.com", texto)
if resultado:
    print("Email encontrado!")
    print(resultado.group())  # Mostra o texto encontrado
```

## Metacaracteres Básicos

```python
# Metacaracteres mais comuns
# . (ponto) - qualquer caractere exceto nova linha
# ^ - início da string
# $ - final da string
# * - 0 ou mais repetições
# + - 1 ou mais repetições
# ? - 0 ou 1 repetição
# [] - conjunto de caracteres
# | - ou (alternativa)

# Exemplos
re.search(r"^O", texto)       # Começa com "O"
re.search(r"com$", texto)     # Termina com "com"
re.search(r"e.emplo", texto)  # "e" seguido de qualquer caractere, e "emplo"
```

## Conjuntos de Caracteres

```python
# [abc] - qualquer caractere entre a, b ou c
# [a-z] - qualquer letra minúscula
# [A-Z] - qualquer letra maiúscula
# [0-9] - qualquer dígito
# [^abc] - qualquer caractere exceto a, b ou c

# Exemplos
re.findall(r"[aeiou]", "Olá Mundo")  # Encontra todas as vogais
re.findall(r"[0-9]+", "Tenho 25 anos e 3 filhos")  # Encontra números
```

## Quantificadores

```python
# Quantificar repetições
# {n} - exatamente n repetições
# {n,} - n ou mais repetições
# {n,m} - entre n e m repetições

telefone = "O número é 123-456-7890"
re.search(r"\d{3}-\d{3}-\d{4}", telefone)  # Encontra o número de telefone
```

## Atalhos para Classes de Caracteres

```python
# \d - dígito [0-9]
# \D - não-dígito [^0-9]
# \w - caractere de palavra [a-zA-Z0-9_]
# \W - não-caractere de palavra
# \s - espaço em branco (espaço, tab, nova linha)
# \S - não-espaço em branco

# Encontrar todas as palavras
palavras = re.findall(r"\w+", "Olá, como estás?")  # ['Olá', 'como', 'estás']

# Encontrar todos os dígitos
digitos = re.findall(r"\d", "Tenho 25 anos")  # ['2', '5']
```

## Grupos de Captura

```python
# Usar parênteses para criar grupos de captura

email = "Contacte-me em user@example.com"
padrao = r"(\w+)@(\w+)\.(\w+)"
resultado = re.search(padrao, email)

if resultado:
    nome_usuario = resultado.group(1)  # "user"
    dominio = resultado.group(2)       # "example"
    tld = resultado.group(3)           # "com"
    email_completo = resultado.group(0)  # "user@example.com"
```

## Substituições

```python
# Substituir texto usando regex
texto = "Meu número é 123-456-7890"
novo_texto = re.sub(r"\d{3}-\d{3}-\d{4}", "XXX-XXX-XXXX", texto)
# Resultado: "Meu número é XXX-XXX-XXXX"

# Substituição com referência a grupos
html = "<div>Título</div>"
novo_html = re.sub(r"<div>(.*?)</div>", r"<h1>\1</h1>", html)
# Resultado: "<h1>Título</h1>"
```

## Exemplo Prático: Validação de Email

```python
import re

def valida_email(email):
    padrao = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(padrao, email):
        return True
    return False

emails = ["user@example.com", "invalid@", "nome.sobrenome@empresa.com"]

for email in emails:
    if valida_email(email):
        print(f"{email} é válido")
    else:
        print(f"{email} não é válido")
```
