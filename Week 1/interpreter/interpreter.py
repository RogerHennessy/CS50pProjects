# Roger Hennessy
# 08-09-2023

# Create our main()
def main():
    # Here we will get input from the user and call calculator()
    userInput = input("Please enter your math question: ")

    # Theres an issue if the user does something normal like 1+1 instead of 1 + 1
    # Code breaks if user doesn't enter spaces between 1 + 1, eg 1+1
    # Will come back later and fix it.
    x, y, z = userInput.split(" ")

    # Pass userInput to calculator()
    calculator(x,y,z)


def calculator(a,b,c):
    # Here we will parse the problem and output the results.
    n1 = float(a)
    n2 = float(c)

    if (b == "+"):
        print (n1+n2)
    elif(b == "-"):
        print(n1-n2)
    elif(b == "x" or b == "X" or b == "*"):
        print(n1*n2)
    elif(b == "/"):
        print(round(n1/n2, 2))
    else:
        print ("Unknown input. Try again")


# Here we will call main()
if __name__ == "__main__":
    main()