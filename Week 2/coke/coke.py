# Roger Hennessy
# 11-09-2023

# Create main()
def main():

    # Here we will ask for user input and call vending_machine
    vending_machine()

def vending_machine():

    # Here we will loop until the user puts in enough, 50c, money.
    # Then we will give change.
    total_amount = 50

    while total_amount > 0:
        print ("Amount Due:", total_amount)
        inserted_amount = int(input("Insert Coin:"))

        # Check for right amount of money, theres no 32 cent coin!!
        if(inserted_amount == 5 or inserted_amount == 10 or inserted_amount == 25):
            total_amount -= inserted_amount

            if(total_amount <= 0):
                print ("Change Owed:", abs(total_amount))


# Here we will call main()
if __name__ == "__main__":
    main()

