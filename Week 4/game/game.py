# Roger Hennessy
# 04 - 10 - 2023

import random
import sys

# Create main()
def main():
    # Call our guessing game function()
    game_guesser()

def game_guesser():
    # Ask for user input
    while True:
        try:
            # Ask for level
            game_level = int(input("Level: ").strip())

            if game_level > 0:
                # Set the high number to game_level and return the number to be guessed
                correct_num = random.randint(0, (game_level))

                while True:
                    # Play the game
                    user_guess = input("Guess: ").strip()
                    user_guess = int(user_guess)

                    if user_guess == correct_num:
                        print("Just right!")
                        sys.exit()

                    elif user_guess < correct_num:
                        print("Too small!")
                        continue

                    elif user_guess > correct_num:
                        print("Too large!")
                        continue

            # Number is less than 1
            else:
                continue

         # Catch some errors
        except ValueError:
            continue

        except KeyError:
            continue

if __name__ == "__main__":
    main()