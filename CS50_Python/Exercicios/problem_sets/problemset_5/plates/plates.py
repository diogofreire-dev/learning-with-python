def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check if length is between 2 and 6 characters
    if len(s) < 2 or len(s) > 6:
        return False
    
    # Check if the first two characters are letters
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    
    # Check for valid characters (no spaces, punctuation, etc.)
    if not s.isalnum():
        return False
    
    # Check if numbers are at the end and don't start with 0
    i = 0
    while i < len(s):
        if s[i].isdigit():
            # First number can't be '0'
            if s[i] == '0':
                return False
            
            # All remaining characters must be digits
            for j in range(i, len(s)):
                if not s[j].isdigit():
                    return False
            
            break
        i += 1
    
    return True


if __name__ == "__main__":
    main()