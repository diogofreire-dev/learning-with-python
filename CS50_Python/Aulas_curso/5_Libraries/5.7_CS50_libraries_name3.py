import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is", arg)

# $ file_name.py name1 name2 name3
# Output : 
# Hello, name1 
# Hello, name2
# Hello, name3