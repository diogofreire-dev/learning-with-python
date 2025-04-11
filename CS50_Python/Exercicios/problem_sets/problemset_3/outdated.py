def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    
    while True:
        date = input("Date: ").strip()
        
        try:
            # Check if input is in MM/DD/YYYY format
            if "/" in date:
                month, day, year = date.split("/")
                month = int(month)
                day = int(day)
                year = int(year)
                
                # Validate month and day
                if month < 1 or month > 12 or day < 1 or day > 31:
                    continue
                
                print(f"{year:04d}-{month:02d}-{day:02d}")
                break
                
            # Check if input is in "Month DD, YYYY" format
            elif "," in date:
                # Split the date into month_name+day and year
                month_day, year = date.split(",")
                month_name, day = month_day.rsplit(" ", 1)
                month_name = month_name.strip()
                day = int(day.strip())
                year = int(year.strip())
                
                # Find the month number from the month name
                if month_name in months:
                    month = months.index(month_name) + 1
                else:
                    continue
                
                # Validate day
                if day < 1 or day > 31:
                    continue
                
                print(f"{year:04d}-{month:02d}-{day:02d}")
                break
                
        except ValueError:
            # If any conversion fails, prompt again
            continue

if __name__ == "__main__":
    main()