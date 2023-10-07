# Roger Hennessy
# 30-09-2032

# import emoji
import emoji

# Create main()
def main():

    # Call emoji_maker()
    emoji_maker()

# Create emoji_maker()
def emoji_maker():
    # Get the user input and then return an emoji
    user_emoji = input("Input:").strip()

    print("Output:", emoji.emojize(user_emoji, language='alias'))

# Call main()
if __name__ == "__main__":
    main()
