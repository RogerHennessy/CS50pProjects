# Roger Hennessy
# 17 - 10 - 2023

import sys
import csv
from tabulate import tabulate

# Create main()
def main():
    # Here check the arguments
    if len(sys.argv) < 2:
         sys.exit("Too few arguments")

    elif len(sys.argv) > 2:
         sys.exit("Too many arguments")

    # Check if CSV file
    if not sys.argv[1][-4:] == ".csv":
         sys.exit("Incorrect file type.")

    # call our file_length()
    table_formatter(sys.argv[1])

# Create table_formatter
def table_formatter(menu):

    # Check if file is found
    try:
        line_count = 0
        # Run through the file to count the lines.
        with open (menu, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            headers = "keys"

            # Maybe add function to change table format at runtime.
            # tablefmt = sys.argv [2]
            tablefmt = "grid"
            print(tabulate((reader), headers, tablefmt))

    except FileNotFoundError:
         sys.exit("File does not exist")

# Call our main()
if __name__ == "__main__":
    main()