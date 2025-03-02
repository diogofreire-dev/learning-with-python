import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments") # sys.exit() is used to exit the program
elif len(sys.argv) > 2:
    sys.exit("Too many arguments") 

print("Hello,", sys.argv[1])   

# $ file_name.py name
# Output : 
# Hello, name