# Roger Hennessy
# 07-10-2023

# Make main()
def main():
    # Here we will ask for user input and send to checkInput()
    greet = (input("Greeting: ")).lower().strip()
    
    print(f"${value(greet)}")

# Make checkInput()
def value(greeting):

    # Check for hello
    if ("hello" in greeting):
        return 0

    # Check for h being the first letter
    elif (greeting[0] == "h"):
        return 20

    # Catch all for anything else
    else:
        return 100

# Call main()
if __name__ == "__main__":
    main()