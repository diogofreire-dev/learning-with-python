# Ask user for their name
name = input("What's your name? ")

# Remove whitespace "strip()" from str and capitalize "title()" user's name
name = name.strip().title()

# Split user's name into first and last name
first, last= name.split(" ")

# Say hello to user
print("hello, " + first)
