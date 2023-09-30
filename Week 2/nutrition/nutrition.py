# Roger Hennessy
# 20 - 09 - 2023

# Create main()
def main():

    # Ask for input
    food_name = input ("Item: ").lower()
    calories_amount(food_name)

# Create calories_amount()
def calories_amount(item):

    # Create a dict for the items
    food_dict = {
        "apple":130,
        "avocado":50,
        "banana":110,
        "cantaloupe":50,
        "grapefruit":60,
        "grapes":90,
        "honeydew melon":50,
        "kiwifruit":90,
        "lemon":15,
        "lime":20,
        "nectarine":60,
        "orange":90,
        "peach":80,
        "pear":100,
        "plums":70,
        "strawberries":50,
        "sweet cherries":100,
        "tangerine":50,
        "watermelon":50
    }
    # Search for users item
    if item in food_dict:
        print ("Calories: ", str(food_dict[item]))
    else:
        return()



# Call main()
if __name__ == "__main__":
    main()

