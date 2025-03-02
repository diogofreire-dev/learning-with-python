import sys

try:
    print("Hello, my name is", sys.argv[1])
except IndexError:
    print("You must provide a name as an argument")

# file_name.py Name
# Output:
# Hello, my name is Name