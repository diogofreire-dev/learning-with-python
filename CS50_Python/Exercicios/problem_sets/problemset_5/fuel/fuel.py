def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            result = gauge(percentage)
            print(result)
            break
        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    x, y = fraction.split("/")
    
    # Convert X and Y to integers
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        raise ValueError
    
    # Check for zero division (verificação deve vir antes!)
    if y == 0:
        raise ZeroDivisionError
    
    # Check if X is greater than Y
    if x > y:
        raise ValueError
    
    # Calculate the percentage
    percentage = round((x / y) * 100)
    
    return percentage


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()