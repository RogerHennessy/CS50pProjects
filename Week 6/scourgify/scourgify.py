# Roger Hennessy
# 17 - 10 - 2023

import sys
import csv
from tabulate import tabulate

# Create main()
def main():
    # Here check the arguments
    if len(sys.argv) < 3:
         sys.exit("Too few arguments")

    elif len(sys.argv) > 3:
         sys.exit("Too many arguments")

    # Check if CSV file
    if not (sys.argv[1][-4:] == ".csv"):
         sys.exit("Incorrect file type.")

    # call our file_length()
    scourgifier(sys.argv[1], sys.argv[2])

# Create table_formatter
def scourgifier(before, after):

    # Check if file is found
    try:
        # Run through the file and write it to another.
        with open (before, "r") as csvfileread:
            reader = csv.DictReader(csvfileread)

            # Open our file that we will write to
            with open(after, "w") as csvfilewrite:
                # Setup the fieldnames
                fieldnames = ["first", "last", "house"]

                writer = csv.DictWriter(csvfilewrite, fieldnames = fieldnames)
                writer.writeheader()

                # Run through and write each row. "Cleaning" the file.
                for rows in reader:
                    # Split the first value into surname and forename.
                    last_name, first_name = rows["name"].split(", ")
                    house = rows["house"]

                    # Write the new format
                    writer.writerow({"first": first_name, "last": last_name, "house": house,})

    except FileNotFoundError:
         sys.exit(f"Could not read {before}")

# Call our main()
if __name__ == "__main__":
    main()