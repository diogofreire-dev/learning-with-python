import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    available_fonts = figlet.getFonts()

    # Check command line arguments
    if len(sys.argv) == 1:
        # Zero arguments - use random font
        selected_font = random.choice(available_fonts)
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        # Two arguments - check if second arg is a valid font
        if sys.argv[2] in available_fonts:
            selected_font = sys.argv[2]
        else:
            sys.exit("Invalid font name")
    else:
        # Invalid arguments
        sys.exit("Invalid usage")
    
    # Set the font
    figlet.setFont(font=selected_font)
    
    # Get text from user
    text = input("Input: ")
    
    # Print the text in the selected font
    print(figlet.renderText(text))

if __name__ == "__main__":
    main()