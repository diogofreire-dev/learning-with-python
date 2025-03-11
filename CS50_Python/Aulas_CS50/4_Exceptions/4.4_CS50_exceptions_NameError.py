try:
    x = int(input("Wha's x? "))
except ValueError:
    print("x is not an integer")

print(f"x is {x}")