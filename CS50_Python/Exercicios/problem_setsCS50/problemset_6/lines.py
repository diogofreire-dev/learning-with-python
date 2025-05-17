import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    file_name = sys.argv[1]
    
    if not file_name.endswith(".py"):
        sys.exit("Not a Python file")
    
    try:
        # Count lines of code
        line_count = count_lines(file_name)
        print(line_count)
    except FileNotFoundError:
        sys.exit("File does not exist")

def count_lines(file_name):
    """
    Count the number of lines of code in a Python file,
    excluding comments and blank lines.
    """
    count = 0
    
    with open(file_name, "r") as file:
        for line in file:
            # Skip blank lines (lines with only whitespace)
            if line.strip() == "":
                continue
            
            # Skip comment lines (lines that start with # after stripping whitespace)
            if line.lstrip().startswith("#"):
                continue
            
            # If we reach here, it's a valid line of code
            count += 1
    
    return count

if __name__ == "__main__":
    main()