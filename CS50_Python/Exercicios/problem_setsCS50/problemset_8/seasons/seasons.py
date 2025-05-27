from datetime import date
import sys
import inflect

def main():
    birth_date = get_birthdate() 
    minutes = calculate_age_in_minutes(birth_date) # Calculate age in minutes
    words = convert_to_words(minutes) # Convert to English words
    print(words.capitalize())

def get_birthdate():
    """Prompt user for birthdate and validate format"""
    try:
        date_str = input("Date of Birth: ")
        # Parse the date string
        year, month, day = map(int, date_str.split('-'))
        birth_date = date(year, month, day)
        return birth_date
    except (ValueError, TypeError):
        sys.exit("Invalid date format")

def calculate_age_in_minutes(birth_date):
    """Calculate age in minutes from birth_date to today"""
    today = date.today()
    
    # Ensure birth_date is not in the future
    if birth_date > today:
        sys.exit("Birth date cannot be in the future")
    
    delta = today - birth_date # Calculate the difference
    minutes = delta.days * 24 * 60 # Convert to minutes (days * 24 hours * 60 minutes)
    return minutes

def convert_to_words(number):
    """Convert number to English words without 'and'"""
    p = inflect.engine()
    words = p.number_to_words(number, andword="")
    # Remove any remaining 'and' that might appear
    words = words.replace(" and ", " ")
    return words

if __name__ == "__main__":
    main()