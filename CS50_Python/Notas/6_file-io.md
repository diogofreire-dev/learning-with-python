# Python File I/O

## Abrir e Fechar Arquivos

Em Python, usamos a função `open()` para trabalhar com arquivos.

```python
# Abrir um arquivo para leitura
arquivo = open("dados.txt", "r")
conteudo = arquivo.read()
arquivo.close()  # Importante fechar o arquivo

# Método mais seguro usando 'with' (fecha automaticamente)
with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
```

## Modos de Abertura

```python
# Modos básicos
"r"  # Leitura (read)
"w"  # Escrita (write) - cria novo ou sobrescreve
"a"  # Adicionar ao final (append)
```

## Leitura de Arquivos

```python
# Ler arquivo inteiro
with open("exemplo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# Ler linha por linha
with open("exemplo.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())  # strip() remove \n no final
```

## Escrita em Arquivos

```python
# Escrever em um arquivo
with open("saida.txt", "w") as arquivo:
    arquivo.write("Olá, mundo!\n")
    arquivo.write("Esta é a segunda linha.")
    
# Adicionar ao final do arquivo
with open("saida.txt", "a") as arquivo:
    arquivo.write("\nEsta linha será adicionada ao final.")
```

## Exemplo Prático: Lista de Nomes

```python
# Guardar nomes em um arquivo
nomes = ["Ana", "Carlos", "Maria", "João"]

with open("nomes.txt", "w") as arquivo:
    for nome in nomes:
        arquivo.write(nome + "\n")

# Ler nomes do arquivo
with open("nomes.txt", "r") as arquivo:
    lista_nomes = []
    for linha in arquivo:
        lista_nomes.append(linha.strip())
    
    print(lista_nomes)  # ['Ana', 'Carlos', 'Maria', 'João']
```

## Trabalhando com Arquivos CSV

```python
import csv

# Ler arquivo CSV
with open("alunos.csv", "r") as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)  # linha é uma lista com os valores

# Escrever arquivo CSV
alunos = [
    ["Nome", "Idade"],
    ["Ana", "20"],
    ["Carlos", "22"]
]

with open("novos_alunos.csv", "w") as arquivo:
    escritor = csv.writer(arquivo)
    for aluno in alunos:
        escritor.writerow(aluno)
```

## Tratamento de Erros Básico

```python
try:
    with open("arquivo_inexistente.txt", "r") as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError:
    print("O arquivo não existe!")
```
