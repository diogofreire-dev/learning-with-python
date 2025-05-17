import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    # Regular expression to match time formats
    # Group 1: Hour (first time)
    # Group 2: Minutes (first time) - optional
    # Group 3: AM/PM (first time)
    # Group 4: Hour (second time)
    # Group 5: Minutes (second time) - optional
    # Group 6: AM/PM (second time)
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    match = re.search(pattern, s)
    
    if not match:
        raise ValueError("Invalid format")
    
    # Extract the matched groups
    hour1, minute1, period1, hour2, minute2, period2 = match.groups()
    
    # Convert to integers
    hour1 = int(hour1)
    hour2 = int(hour2)
    
    # Set minutes to 00 if not provided
    minute1 = int(minute1) if minute1 else 0
    minute2 = int(minute2) if minute2 else 0
    
    # Validate hours and minutes
    if hour1 < 1 or hour1 > 12 or hour2 < 1 or hour2 > 12:
        raise ValueError("Invalid hour")
    if minute1 < 0 or minute1 > 59 or minute2 < 0 or minute2 > 59:
        raise ValueError("Invalid minute")
    
    # Convert to 24-hour format
    hour1_24 = convert_to_24_hour(hour1, period1)
    hour2_24 = convert_to_24_hour(hour2, period2)
    
    # Format the output string
    return f"{hour1_24:02}:{minute1:02} to {hour2_24:02}:{minute2:02}"

def convert_to_24_hour(hour, period):
    """Convert 12-hour format to 24-hour format."""
    if period == "AM":
        if hour == 12:
            return 0  # 12 AM is 00:00 in 24-hour format
        return hour
    else:  # PM
        if hour == 12:
            return 12  # 12 PM is 12:00 in 24-hour format
        return hour + 12

if __name__ == "__main__":
    main()