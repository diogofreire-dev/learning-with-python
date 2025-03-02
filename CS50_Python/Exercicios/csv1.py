from csv import DictReader

with open("dados.csv", newline='', encoding='utf-8') as ficheiro:
    leitor_csv = DictReader(ficheiro)  # Lê o CSV como dicionários

    for linha in leitor_csv:
        print(linha)  # Cada linha será um dicionário

"""
Se o ficheiro "dados.csv" for este:

Nome,Idade,Cidade
João,25,Lisboa
Maria,30,Porto
Carlos,22,Coimbra

"""

"""
O output será:

{'Nome': 'João', 'Idade': '25', 'Cidade': 'Lisboa'}
{'Nome': 'Maria', 'Idade': '30', 'Cidade': 'Porto'}
{'Nome': 'Carlos', 'Idade': '22', 'Cidade': 'Coimbra'}

"""