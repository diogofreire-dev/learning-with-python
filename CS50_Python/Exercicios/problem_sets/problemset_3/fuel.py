def main():
    while True:
        try:
            # Prompt user for input
            fraction = input("Fraction: ")
            
            # Split the input into numerator and denominator
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)
            
            # Check if x is greater than y
            if x > y:
                continue
                
            # Calculate percentage
            percentage = round((x / y) * 100)
            
            # Determine output based on percentage
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")
                
            break
            
        except ValueError:
            # Handle case where x or y is not an integer or input format is wrong
            continue
        except ZeroDivisionError:
            # Handle case where y is 0
            continue

if __name__ == "__main__":
    main()