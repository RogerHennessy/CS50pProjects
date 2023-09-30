# Roger Hennessy
# 07-09-2023

# Create our main()
def main():
    # Get input
    mass = int(input("Please enter the mass you wish to convert: "))

    # Call joulesConvertor()
    joulesConvertor(mass)

# Create joulesConvertor()
def joulesConvertor(mass):
    # Make c squared
    c = 300000000 * 300000000

    # Convert to Joules and print.
    print ("The amount of Joules is :", mass * c)

# Call main()
if __name__ == "__main__":
    main()