from random import randint

# Loop
while True:
    # Ask: roll the dice?
    user_input = input("Roll the dice? (y/n): ").lower().strip()
    # If user enters y
    if user_input == "y":
        # Generate two random numbers
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        # Print them eg. (23, 99)
        print(f"({num1}, {num2})")

        # If user enters n
    elif user_input == "n":
        # Print thank you message
        print("Thanks for playing!")
        break #Terminate
    else:
        print("Invalid choice!") #Print invalid code


