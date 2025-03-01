def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("Wha's x? "))
        except ValueError:
            pass # pass fará com que o programa continue a executar sem parar 
        else:
            return x 
        # aqui não irá ser preciso do break porque o return já 
        # irá fazer com que a função termine
        
main()