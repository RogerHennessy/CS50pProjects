# Roger Hennessy
# 08-09-2023

# Make main()
def main():
    # Here we will ask for user input and send to checkInput()
    salutation = input("How do you greet people: ")
    checkInput(salutation)

# Make checkInput()
def checkInput(greeting):

    # Make it case insensitive
    greeting = greeting.lower().lstrip()

    # Check for hello
    if ("hello" in greeting):
        print ("$0")

    # Check for h being the first letter
    elif (greeting[0] == "h"):
        print ("$20")

    # Catch all for anything else
    else:
        print ("$100")

# Call main()
if __name__ == "__main__":
    main()