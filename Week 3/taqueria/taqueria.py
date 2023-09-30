# Roger Hennessy
# 21 - 09 - 2023

# Here we will make our main()
def main():

    # Here we will call total_bill()
    total_bill()

def total_bill():

    # Start the bill at 0
    bill = 0.0
     # Create a dict for the items
    food_dict ={
        "Baja Taco":4.00,
        "Burrito":7.50,
        "Bowl":8.50,
        "Nachos":11.00,
        "Quesadilla":8.50,
        "Super Burrito":8.50,
        "Super Quesadilla":9.50,
        "Taco":3.00,
        "Tortilla Salad":8.00
    }

    # Loop as long as the user is "eating"
    eating = True
    while eating:
        try:
            # Get user input
            item = input ("Item: ").title()

            # Search for users item
            if item in food_dict:
                bill += float(food_dict[item])
                print (f"Total: ${bill:.2f}")
            else:
                eating = True

        # Catch some errors
        except ValueError:
            eating = True

        except KeyError:
            eating = True

        except EOFError:
            eating = False

# Call main()
if __name__ == "__main__":
    main()


