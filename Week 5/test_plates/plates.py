# Roger Hennessy
# 08-10-2023

# Create main()
def main():

    # Ask for user input and pass it to is_vaild()
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
        
    else:
        print("Invalid")


# Create is_vaild()
def is_valid(user_plate):

    # “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    if(len(user_plate) >= 2 and len(user_plate) <= 6):

        # That the length is ok, make a list
        user_list = list(user_plate)

        # Check if all letters
        if(user_plate.isalpha()):
            return True

        # “All vanity plates must start with at least two letters.”
        elif(user_list[0].isalpha() and user_list[1].isalpha() and user_list[-1].isnumeric()):

            # Look for non numeric/non letter
            for i in range(len(user_list)):
                if(user_list[i].isalpha() or user_list[i].isnumeric()):
                    no_punc = True
                else:
                    return False

            # This is very ugly code that works, as in it passes the test, but I need to come back and fix this code.
            # It's not good.
            if(no_punc):
                # Next Check - The first number used cannot be a ‘0’
                if (user_list[2].isnumeric() and user_list[2] != "0"):
                    if(user_list[-2].isnumeric()):
                        if(user_list[-2].isnumeric()):
                            return True
                        else:
                            return False
                    else:
                        return False

                # First number can't be a zero
                elif (user_list[2] == "0"):
                    return False

                # Lets check if it is a number, if so it can't be zero and the following must be numbers.
                elif (user_list[3].isnumeric() and user_list[3] != "0"):
                    if(user_list[-3].isnumeric()):
                        if(user_list[-2].isnumeric()):
                            return True
                        else:
                            return False
                    else:
                        return False

                # First number can't be a zero
                elif (user_list[3] == "0"):
                    return False

                return True

            # First two characters not Letters and last is not digit
            else:
                return False

    # Too short or too long
    else:
        return False

# Call our main()
if __name__ == "__main__":
    main()