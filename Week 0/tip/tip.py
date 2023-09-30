# Roger Hennessy
# 07-09-2023

## Create our main()
def main():
    # Get input from the user for amount and percentage
    dollars = dollarsToFloat(input("How much was the meal? "))
    percent = percentToFloat(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# Create dollarsToFloat
def dollarsToFloat(d):
    # Remove the dollor and change to a float
    d = d.removeprefix("$")

    # Return
    return float (d)


# Create percentToFloat
def percentToFloat(p):
    # Remove % and change to float
    p = float(p.removesuffix("%"))

    # Return
    return float (p/100)

# Call main()
if __name__ == "__main__":
    main()