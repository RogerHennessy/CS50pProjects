# Roger Hennessy
# 05-10-2023

import random
import sys

# Create main()
def main():
    # Here we will call get_level()
    # Here we will output the questions and check if they are right
    tries = 3
    score = 0
    questions_answered = 0

    level = get_level()
    x,y = generate_integer(level)

    while True:
        try:
            # ten_questions(x,y)
            user_guess = int(input(f"{x} + {y} =").strip())
            answer = x + y

            # Check answer
            if user_guess == answer:
                # Get next question
                print(f"You're right")
                x,y = generate_integer(level)
                score += 1
                questions_answered += 1

                if questions_answered == 10:
                    print(f"Score: {score}")
                    sys.exit()

            if user_guess != answer:
                # Repeat question
                tries -= 1
                print("EEE")
                # Show answer, reset tries and move on to next question
                if tries == 0:
                    print(f"{x}+{y} = {(x+y)}")
                    tries = 3
                    questions_answered += 1
                    x,y = generate_integer(level)

            if questions_answered == 10:
                    print(f"Score: {score}")
                    sys.exit()

        # Catch some errors
        except (ValueError, KeyError, NameError):
            print("EEE")
            tries -= 1
            continue

# Create get_level()
def get_level():
    # Get input from the user
    # and pass it to generate_integer()
    while True:
        try:
            game_level = int(input("Level: "))

            if game_level == 1 or game_level == 2 or game_level == 3:
                return game_level

            else:
                continue

        # Catch some errors
        except (ValueError, KeyError, NameError):
            continue

# Create generate_integer()
def generate_integer(level):
    # Maybe have two lists of 10?
    # Or make a new var on the fly
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)

    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)

    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)

    return x,y

# Call main()
if __name__ == "__main__":
    main()
