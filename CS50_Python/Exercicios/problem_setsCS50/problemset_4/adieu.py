import inflect

# Create an inflect engine
p = inflect.engine()

# List to store names
names = []

# Prompt for names until EOF
try:
    while True:
        name = input("Name: ")
        names.append(name)
except EOFError:
    print()  # for a clean newline after Ctrl-D/Z

# Join names using inflect
formatted_names = p.join(names)

# Print the final message
print(f"Adieu, adieu, to {formatted_names}")
