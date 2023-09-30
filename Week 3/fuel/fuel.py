# Roger Hennessy
# 20 - 09 - 2023

# Make main()
def main():
    # Call our fuel_gauge()
    fuel_gauge()

# Make fuel_gauge()
def fuel_gauge():
    incorrect = True

    # Ask the user for input, loop until correct input
    while incorrect:
        # Test the input and catch errors
        try:
            user_input = input("Fraction: ")
            x, y = user_input.split("/")

            # Make it a percentage
            output_value = float(int(x)/int(y))*100

            output_value = round(output_value)

            # Check the range
            if (output_value > 100):
                incorrect = True
            elif (output_value < 99 and output_value > 1):
                print(str(int(output_value)) + "%")
                incorrect = False
            elif (output_value <= 1):
                print ("E")
                incorrect = False
            elif (output_value >= 99):
                print("F")
                incorrect = False

        except ValueError:
            incorrect = True

        except ZeroDivisionError:
            incorrect = True

# Call main()
if __name__ == "__main__":
    main()