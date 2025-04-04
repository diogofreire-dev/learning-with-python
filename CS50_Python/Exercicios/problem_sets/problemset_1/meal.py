def main():
    # Prompt the user for the time
    time_str = input("What time is it? ")
    
    # Convert the time to a float representing hours
    time = convert(time_str)
    
    # Determine if it's meal time
    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")
    # No output if it's not meal time

def convert(time):
    # Split the time string into hours and minutes
    parts = time.split(":")
    hours = int(parts[0])
    minutes = int(parts[1])
    
    # Convert minutes to a fraction of an hour
    # 60 minutes = 1 hour, so minutes/60 = fraction of an hour
    return hours + minutes / 60

if __name__ == "__main__":
    main()