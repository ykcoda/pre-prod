from random import randint

counter = 0
# Loop
while True:
    
    # Ask: roll the dice?
    user_input = input("Roll the dice? (y/n): ").lower().strip()
    # If user enters y
    if user_input == "y":
        # Ask: How many dice do you want to roll
        num_of_dice = int(input("How many dice do you want to role? "))
        for n in range(0, num_of_dice):
            # Generate two random numbers
            die1 = randint(1, 100)
            die2 = randint(1, 100)
            # Print them eg. (23, 99)
            print(f"({die1}, {die2})")
        counter += 1
        # If user enters n
    elif user_input == "n":
        # Print thank you message
        print("Thanks for playing!")
        break  # Terminate
    else:
        print("Invalid choice!")  # Print invalid code

print(f"User rolled the dice {counter}x.")