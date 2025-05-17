def main():
    # Prompt the user for input text
    text = input("Input: ")
    
    # Initialize empty string for the result
    result = ""
    
    # Iterate through each character in the input text
    for char in text:
        # If the character is not a vowel, add it to the result
        if char.lower() not in ['a', 'e', 'i', 'o', 'u']:
            result += char
    
    # Output the result
    print("Output:", result)

if __name__ == "__main__":
    main()