from tabulate import tabulate
import csv
import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    file_name = sys.argv[1]
    
    if not file_name.endswith(".csv"):
        sys.exit("Not a CSV file") 
    
    try:
        with open(file_name) as file:
            reader = csv.reader(file) # Lê o arquivo CSV
            data = list(reader) # Converte os dados lidos numa "lista(list)"

        table = tabulate(data[1:], data[0], tablefmt="grid") # Formatação da tabela
        print(table) # Apresenta a tabela no terminal

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == '__main__':
    main()