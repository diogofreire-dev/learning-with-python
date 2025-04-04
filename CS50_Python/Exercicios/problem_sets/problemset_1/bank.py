def main():
    # Prompt the user for a greeting
    greeting = input("Greeting: ").lstrip().lower()
    
    # Check the greeting and determine the amount
    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")

if __name__ == "__main__":
    main()