# Roger Hennessy
# 10-09-2023
# 11-09-2023

# Create main()
def main():

    # Here we will get the user input and send it to snakeCase()
    camelCase = input("Please enter camel Case:")

    snakeCase(camelCase)

# Create snakeCase()
def snakeCase(snake_case):

    # Iterate through the string, once upper is found,
    # add an underscore and make it lowercase
    # Else keep printing the letters.
    for c in snake_case:
        if(c.isupper()):
            print("_" + c.lower(), end = "")

        else:
            print(c, end="")


# Call main()
if __name__ == "__main__":
    main()