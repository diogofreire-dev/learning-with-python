def main():
    # Menu with prices
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    total = 0.0

    # Keep prompting user for items until control-d (EOF) or empty input
    try:
        while True:
            item = input("Item: ").title()

            if item in menu:
                total += menu[item]
                print(f"${total:.2f}")

    except EOFError:
        # End program when control-d is pressed
        pass
    
    print()  # Print a newline for cleaner output
    return

if __name__ == "__main__":
    main()