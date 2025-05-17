import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    try:
        # Create a list to store the processed data
        students = []
        
        with open(input_file) as file:
            reader = csv.DictReader(file)
            
            # Process every row in the input file
            # Process the data and add it to the list
            for row in reader:
                last, first = row["name"].strip('"').split(", ")
                
                students.append({
                    "first": first,
                    "last": last,
                    "house": row["house"]
                })
        
        with open(output_file, "w", newline="") as file:
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            writer.writeheader()
            
            for student in students:
                writer.writerow(student)
                
    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")

if __name__ == "__main__":
    main()