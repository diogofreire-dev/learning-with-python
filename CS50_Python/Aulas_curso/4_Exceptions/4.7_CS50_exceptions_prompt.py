def main():
    x = get_int("Digite um número inteiro: ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
        except ValueError:
            pass  # pass fará com que o programa continue a executar sem parar
        else:
            return x

main()