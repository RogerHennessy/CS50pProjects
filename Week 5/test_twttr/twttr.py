# Roger Hennessy
# 07-10-2023

# Create main()
def main():
    # Here we will call remove_vowels()

    user_input = input("Input: ")
    output = shorten(user_input)
    print(f"Output: {output}")

# Create remove_vowels()
def shorten(user_string):
    # Here we will loop through the string and remove all the vowels

    # Find and remove the vowels, in a loop.
    for c in user_string:
        # Just a bunch of ifs and elifs.
        # Not sure how to make it shorter.
        if(c == "a" or c == "A"):
            user_string = user_string.replace("a","")
            user_string = user_string.replace("A","")

        if(c == "e" or c == "E"):
            user_string = user_string.replace("e","")
            user_string = user_string.replace("E","")

        if(c == "i" or c == "I"):
            user_string = user_string.replace("i","")
            user_string = user_string.replace("I","")

        if(c == "o" or c == "O"):
            user_string = user_string.replace("o","")
            user_string = user_string.replace("O","")

        if(c == "u" or c == "U"):
            user_string = user_string.replace("u","")
            user_string = user_string.replace("U","")

    return user_string

# Call main()
if __name__ == "__main__":
    main()
