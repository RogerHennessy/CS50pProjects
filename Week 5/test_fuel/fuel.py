# Roger Hennessy
# 20 - 09 - 2023

# Make main()
def main():
    fraction = input("Fraction: ")
    percent = convert(fraction)
    print(gauge(percent))

def convert(fraction):
    # Split into x and y
    x,y = fraction.split("/")

    # Check if x is greater than y
    if int(x)/int(y) > 1:
        raise ValueError

    # is y 0
    elif int(y) == 0:
        raise ZeroDivisionError

    # Return our percentage
    return int(int(x)/int(y) * 100)

def gauge(percentage):
    try:
        if 0 <= percentage <= 1:
            return "E"

        elif 99 <= percentage <= 100:
            return "F"

        elif 1 <= percentage <= 99:
            return (f"{int(percentage)}%")

        else:
            raise TypeError

    except TypeError:
        pass


if __name__ == "__main__":
    main()
