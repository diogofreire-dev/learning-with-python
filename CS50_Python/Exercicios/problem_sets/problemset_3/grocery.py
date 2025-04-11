def main():
    # Initialize an empty dictionary to store grocery items and their counts
    grocery_list = {}
    
    # Prompt user for items until control-d is entered
    try:
        while True:
            item = input().strip().lower()
            
            # Add item to dictionary or increment its count
            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1
                
    except EOFError:
        # When user inputs control-d, print the sorted grocery list
        for item in sorted(grocery_list.keys()):
            print(f"{grocery_list[item]} {item.upper()}")

if __name__ == "__main__":
    main()