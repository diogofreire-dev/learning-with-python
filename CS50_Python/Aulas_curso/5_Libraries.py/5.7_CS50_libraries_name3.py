import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is", arg)

# $ 5.6_CS50_libraries_name2.py name1 name2 name3
# Output : 
# Hello, name1 
# Hello, name2
# Hello, name3