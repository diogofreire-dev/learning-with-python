def main():
    print_square(3)

def print_square(size):
    #Vertical
    for i in range(size):
        #Horizontal
        for j in range(size):
            print("#", end="")
        print()

main()