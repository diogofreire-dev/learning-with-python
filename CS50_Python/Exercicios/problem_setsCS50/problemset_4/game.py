import random

def main():
    # Get level from user
    while True:
        try:
            n = int(input("Level: "))
            if n <= 0:
                break
            else:
                continue
        except ValueError:
            continue

    # Generate random number between 1 and n
    secret = random.randint(1, n)

    # Main game loop
    while True:
        # Get guess from user
        try:
            guess = int(input("Guess: "))
            if guess <= 0:
                continue
        except ValueError:
            continue

        # Check guess against secret number
        if guess < secret:
            print("Too small!")
        elif guess > secret:
            print("Too large!")
        else:
            print("Just right!")
            break

if __name__ == "__main__":
    main()