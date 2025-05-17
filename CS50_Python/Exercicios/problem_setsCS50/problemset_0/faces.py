def convert(text):
    # Replace emoticons with emoji descriptions
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

def main():
    # Prompt the user for input
    user_input = input("Input: ")
    
    # Call convert function on the input
    converted_text = convert(user_input)
    
    # Print the result
    print(converted_text)

# Call main function when program is run
if __name__ == "__main__":
    main()