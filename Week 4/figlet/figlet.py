# Roger Hennessy
# 03 - 10 - 2023

from pyfiglet import Figlet
import random
import sys

# Make main()
def main():
    # Call our ascii_art()
    ascii_art()

def ascii_art():
    # Setup figlet
    figlet = Figlet()

    # Return the list of fonts
    fonts_list = figlet.getFonts()

    # No arguments so output random font
    if len(sys.argv) < 2:
        # Ask for user input
        text = input("Input: ")

        # Get a random number to act as our font index
        rand_font = random.randint(0, len(fonts_list))

        # Set the font
        figlet.setFont(font=fonts_list[rand_font])

        # Render the text
        print("Output:", figlet.renderText(text))

    # Check if the arguments match
    elif len(sys.argv) == 3:    # Check length
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":      # Is the first argument vaild
            if str(sys.argv[2]) in fonts_list:      # Is the font vaild
                # Ask for user input
                text = input("Input: ")

                # Get the index of the font
                font_index = fonts_list.index(str(sys.argv[2]))

                # Set the font
                figlet.setFont(font=fonts_list[font_index])

                # Render the text
                print("Output: ")
                print(figlet.renderText(text))

            else:
                sys.exit("Font not found")
        else:
            sys.exit("First argument unknown")
    else:
        sys.exit("Too many arguments")

# Call main()
if __name__ == "__main__":
    main()