import sys
import os
from PIL import Image, ImageOps

def main():
    # Check for correct number of command-line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    # Get file extensions
    input_ext = os.path.splitext(input_file)[1].lower()
    output_ext = os.path.splitext(output_file)[1].lower()
    
    # Check if extensions are valid (.jpg, .jpeg, or .png)
    valid_extensions = [".jpg", ".jpeg", ".png"]
    if input_ext not in valid_extensions:
        sys.exit("Invalid input")
    if output_ext not in valid_extensions:
        sys.exit("Invalid output")
    
    # Check if input and output extensions match
    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")
    
    try:
        # Open input image and shirt image
        input_image = Image.open(input_file)
        shirt_image = Image.open("shirt.png")
        
        # Get shirt size
        shirt_size = shirt_image.size
        
        # Resize and crop input image to match shirt size
        input_image = ImageOps.fit(input_image, shirt_size)
        
        # Overlay shirt on input image
        input_image.paste(shirt_image, (0, 0), shirt_image)
        
        # Save result as output image
        input_image.save(output_file)
        
    except FileNotFoundError:
        sys.exit("Input does not exist")

if __name__ == "__main__":
    main()