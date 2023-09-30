# Roger Hennessy
# 22 - 09 - 2023

# Create main()
def main():
    # Call the grocery_list()
    grocery_list()

def grocery_list():

    # Make our dict_list
    shopping_list = {}

    writing = True
    # Loop while the user is filling out the list
    while writing:
        # Ask for the user input
        try:
            # Get user input
            item = input ("").upper()

            # Search for users item,
            # if it is there, increase the counter
            # else add it to shopping_list
            if item in shopping_list:
                shopping_list[item] += 1

            else:
                shopping_list[item] = 1
                writing = True

        # Catch some errors
        except ValueError:
            writing = True

        except KeyError:
            writing = True

        # I got the following idea from looking online,
        # https://realpython.com/iterate-through-dictionary-python/
        # I still don't fully understand why this works so well.
        # I tried something like
        #   for key in shopping_list:
        #       print(shopping_list[key], " ", key)

        except EOFError:
            # Put the list alphabetically
            sorted_shopping_list = dict(sorted(shopping_list.items()))
            for key, value in sorted_shopping_list.items():
                print(value, key)

            writing = False


# Call main())
if __name__ == "__main__":
    main()
