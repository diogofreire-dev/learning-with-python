def main():
    # Prompt user for input in camel case
    camel = input("camelCase: ")
    
    # Convert to snake case
    snake = ""
    for char in camel:
        if char.isupper():
            snake += "_" + char.lower()
        else:
            snake += char
    
    # Print the snake case version
    print("snake_case", snake)

if __name__ == "__main__":
    main()