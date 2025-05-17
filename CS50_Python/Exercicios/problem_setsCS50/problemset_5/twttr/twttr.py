def main():
    word = input("Input: ")
    print("Output:", shorten(word))


def shorten(word):
    vowels = "AEIOUaeiou"
    result = ""
    for char in word:
        if char not in vowels:
            result += char
    return result


if __name__ == "__main__":
    main()