import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello,", sys.argv[1])

# $ python file_name.py Name
# Output: 
# Generates ASCII art picture of a cow with 
# a message saying "hello, Name".