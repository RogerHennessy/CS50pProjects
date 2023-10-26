# Roger Hennessy
# 17- 10 -2023

import sys

# create main()
def main():
    # Here check the arguments
    if len(sys.argv) < 2:
         sys.exit("Too few arguments")

    elif len(sys.argv) > 2:
         sys.exit("Too many arguments")

    # Check if python file
    if not sys.argv[1][-3:] == ".py":
         sys.exit("Incorrect file type.")

    # call our file_length()
    print(file_length(sys.argv[1]))

# Create file_length
def file_length(document):

    # Check if file is found
    try:
        line_count = 0
        # Run through the file to count the lines.
        with open (document, "r") as file:
            for line in file:
                # Skip comments and whitespace
                if not (line.lstrip().startswith("#") or line.strip() == ""):
                        line_count += 1

    except FileNotFoundError:
         sys.exit("File does not exist")

    # Return the amount of lines.
    return line_count

# Call our main()
if __name__ == "__main__":
    main()
