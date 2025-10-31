# Generate an random number to guess
# Ask: Guess the number between 1 and 100:

# If input is invalid: please enter a valid number

# if number is high: print "Too high!"
# if number is low: print "Too low!"
# if the correct number: "Congratulations! You guessed the number"
from random import randint

random_number = randint(1, 50)

while True:
    try:
        user_number = int(input("Guess the number between 1 and 50: "))
        if user_number == random_number:
            print("Congratulations! You guessed the number")
            break
        elif user_number < random_number:
            print("Too low!")
        else:
            print("Too high!")
    except ValueError:
        print("Please enter a valid number!")    