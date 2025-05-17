import emoji

def main():
    # Prompt user for input
    text = input("Input: ")

    # Print the result
    print(f"Output: {emoji.emojize(text, language="alias")}")

if __name__ == "__main__":
    main()