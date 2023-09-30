# Roger Hennessy
# 28 - 09 - 2023

# Here we will create main()
def main():

    # Call our function
    fix_date()

# Create our function
def fix_date():

    months_list = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    inputting = True
    # Loop while the user is filling out the list
    while inputting:
        # Ask for the user input
        user_date = input("Date: ").strip()

        try:
            # Get user input
            # It's using a word for the month
            if user_date[0].isalpha() and "," in user_date:
                user_date = user_date.replace(",", "").split(" ")
                if user_date[0] in months_list:

                    year = user_date[2]     # Put the year first
                    month = user_date[0]    # Put the month second
                    date = user_date[1]     # Put the date last

                    month = (months_list.index(month)) + 1

            elif "/" in user_date:
                month, date, year = user_date.split("/")

            if(int(month) > 12 or int(date) > 31):
                raise ValueError

        # Catch some errors
        except (AttributeError, ValueError, NameError, KeyError):
            pass

        else:
            print(f"{int(year)}-{int(month):02}-{int(date):02}")
            break


# Call main()
if __name__ == "__main__":
    main()

# This was the hardest for me so far, not to sure why it was so difficult.
#