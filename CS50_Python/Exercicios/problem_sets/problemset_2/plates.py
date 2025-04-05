def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check if plate has between 2 and 6 characters
    if len(s) < 2 or len(s) > 6:
        return False
    
    # Check if the first two characters are letters
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    
    # Check if there are any spaces, periods, or punctuation marks
    if not s.isalnum():
        return False
    
    # Check if numbers are only at the end
    number_started = False
    for i in range(len(s)):
        if s[i].isdigit():
            # First digit cannot be '0'
            if not number_started and s[i] == '0':
                return False
            number_started = True
        elif number_started:
            # If we find a letter after a number, invalid
            return False
    
    return True


main()