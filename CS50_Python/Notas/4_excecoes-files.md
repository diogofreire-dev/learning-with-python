# Exceções e Ficheiros

## Tratamento de Exceções

```python
# Bloco try-except básico
try:
    num = int(input("Digita um número: "))
    resultado = 10 / num
    print(f"10 dividido por {num} é {resultado}")
except ValueError:
    print("Erro: Deves digitar um número válido!")
except ZeroDivisionError:
    print("Erro: Não podes dividir por zero!")
except:
    print("Ocorreu um erro inesperado!")

# Com else e finally
try:
    ficheiro = open("dados.txt", "r")
    conteúdo = ficheiro.read()
except FileNotFoundError:
    print("O ficheiro não foi encontrado!")
else:
    # Executa se não houver exceção
    print(f"Conteúdo: {conteúdo}")
finally:
    # Executa sempre, haja ou não exceção
    try:
        ficheiro.close()
    except:
        pass  # ignore se o ficheiro nunca foi aberto

# Criar exceções personalizadas
class IdadeInvalidaError(Exception):
    pass

def verificar_idade(idade):
    if idade < 0 or idade > 120:
        raise IdadeInvalidaError("A idade deve estar entre 0 e 120")
    return idade

# Usar a exceção personalizada
try:
    idade = verificar_idade(150)
except IdadeInvalidaError as erro:
    print(f"Erro: {erro}")
```

## Trabalhar com Ficheiros

```python
# Abrir e ler um ficheiro
try:
    with open("exemplo.txt", "r", encoding="utf-8") as ficheiro:
        # O bloco 'with' fecha automaticamente o ficheiro
        conteúdo = ficheiro.read()  # ler todo o ficheiro
        print(conteúdo)
except FileNotFoundError:
    print("O ficheiro não existe!")

# Ler linha a linha
with open("exemplo.txt", "r", encoding="utf-8") as ficheiro:
    for linha in ficheiro:
        print(linha.strip())  # strip remove espaços e quebras de linha

# Ler para uma lista de linhas
with open("exemplo.txt", "r", encoding="utf-8") as ficheiro:
    linhas = ficheiro.readlines()
    print(f"O ficheiro tem {len(linhas)} linhas")

# Escrever num ficheiro
with open("novo.txt", "w", encoding="utf-8") as ficheiro:
    ficheiro.write("Primeira linha\n")
    ficheiro.write("Segunda linha\n")

# Adicionar a um ficheiro existente
with open("novo.txt", "a", encoding="utf-8") as ficheiro:
    ficheiro.write("Esta linha é adicionada ao fim\n")

# Trabalhar com ficheiros CSV
import csv

# Ler CSV
with open("dados.csv", "r", encoding="utf-8") as ficheiro:
    leitor = csv.reader(ficheiro)
    for linha in leitor:
        print(f"Coluna 1: {linha[0]}, Coluna 2: {linha[1]}")

# Escrever CSV
dados = [
    ["Nome", "Idade", "Cidade"],
    ["Ana", "25", "Lisboa"],
    ["João", "30", "Porto"]
]

with open("pessoas.csv", "w", newline="", encoding="utf-8") as ficheiro:
    escritor = csv.writer(ficheiro)
    for linha in dados:
        escritor.writerow(linha)
```
