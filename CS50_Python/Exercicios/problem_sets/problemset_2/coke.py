def main():
    # Cost of a bottle of Coke (starts as amount due)
    cost = 50
    
    # Continue accepting coins until enough money is inserted
    while cost > 0:
        # Inform user of amount due
        print(f"Amount Due: {cost}")
        
        # Prompt user to insert a coin
        coin = int(input("Insert Coin: "))
        cost -= coin
        
    # Output the change owed (cost is now zero or negative)
    # Multiply by -1 to convert to a positive number
    print(f"Change Owed: {cost * -1}")

if __name__ == "__main__":
    main()