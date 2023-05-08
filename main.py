import random

def ask_number(min, max):
    number = 0
    while number == 0:
        number_str = input(f"Pick a number between {min} and {max}? ")
        try:
            number = int(number_str)
        except:
            print("Error please enter a number")
        else:
            if number < min or number > max:
                print(f"Please input a number between {min} and {max}.")
                number = 0
    return number


MIN_NUMBER = 1
MAX_NUMBER = 10
MAGIC_NUMBER  = random.randint(MIN_NUMBER, MAX_NUMBER)
NUM_LIVES = 4
number = 0
lives = NUM_LIVES
while not number == MAGIC_NUMBER and lives > 0:
    print(f"You have {lives} lives.")
    number = ask_number(MIN_NUMBER, MAX_NUMBER)
    if number == MAGIC_NUMBER:
        print("You won!")
    elif number > MAGIC_NUMBER:
        print("The magic number is lower")
        lives -= 1
    elif number < MAGIC_NUMBER:
        print("The magic number is greater")
        lives -= 1
if lives == 0:
    print(f"You have lost! The magic number was {MAGIC_NUMBER}.")