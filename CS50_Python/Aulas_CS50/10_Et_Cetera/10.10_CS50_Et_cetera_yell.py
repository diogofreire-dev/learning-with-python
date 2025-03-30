def main():
    yell("This", "is", "CS50")

def yell(*words):
    uppercased = [word.upper() for word in words] # list comprehension which uppercases each word
    print(*uppercased)

if __name__ == "__main__":
    main()


"""
def main():
    yell("This", "is", "CS50")

def yell(*words):
    uppercased = map(str.upper, words) # map function which uppercases each word
    print(*uppercased)

if __name__ == "__main__":
    main()
"""

"""
def main():
    yell("This", "is", "CS50")

def yell(*words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)

if __name__ == "__main__":
    main()
"""


"""
def main():
    yell(["This", "is", "CS50"])

def yell(words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)

if __name__ == "__main__":
    main()
"""