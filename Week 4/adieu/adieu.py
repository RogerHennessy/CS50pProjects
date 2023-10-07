# Roger Hennessy
# 03 - 10 - 2023
# Did this new version after looking around at others on discord.
# Should have done this myself, but was in a rush so the previous code was right, but poorly coded
import inflect

# Make main()
def main():
    # Setup inflect
    global inflect_var
    inflect_var = inflect.engine()

    # Call our function
    adieu()

# Make adieu()
def adieu():
    # Create list for the names
    adieu_name = []
    try:
        while True:
            # Get user input
            adieu_name_temp = input("Name: ").strip().title()
            adieu_name.append(adieu_name_temp)

    # CRTL + D
    except EOFError:
        print()
        print("Adieu, adieu, to", inflect_var.join(adieu_name))

# Call main()
if __name__ == "__main__":
    main()