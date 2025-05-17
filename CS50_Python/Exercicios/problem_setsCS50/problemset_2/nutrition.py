def main():
    # Create a dictionary of fruits and their calorie counts
    fruits = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80
    }
    
    # Prompt the user for a fruit
    fruit = input("Item: ").lower()
    
    # Check if the fruit is in our dictionary
    if fruit in fruits:
        # Output the calorie count
        print(f"Calories: {fruits[fruit]}")

if __name__ == "__main__":
    main()