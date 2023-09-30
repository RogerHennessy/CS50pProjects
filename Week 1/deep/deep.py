# Roger Hennessy
# 07-09-2023

# Create main()
def main():
    # Here ask for input and call deepThoughtMachine()
    userInput = input("What is the answer to the Great Question of Life, the Universe and Everything? ")
    deepThoughtMachine(userInput)

def deepThoughtMachine(answer):
    # Here find out if then input is 42.
    # Remove spaces and make it all lowercase.
    answer = answer.lower().replace(" ","").replace("-","")

    # Will print yes if it matches
    if (answer == "42" or answer == "fortytwo"):
        print ("Yes")

    else:
        print ("No")

# Call main()
if __name__ == "__main__":
    main()
