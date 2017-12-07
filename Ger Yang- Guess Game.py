# Generate a number
# Ask the user for an input(number)
# Does the guess match the number?
# Add "Higher" and "Lower"
# Add 5 guesses

# Choose a number between 1 and 50

print("Welcome to the guessing game!")
print("The computer guesses a number from 1 to 50 and")
print("the user will guess the number")
print("Ready")
print("Begin")

import random

winning_number = random.randint(1,50)
print(winning_number)
player_guess = int(input("Choose a number between 1 and 50"))
def player_guess(winning_number):
    if player_guess == winning_number:
        print("you win!")
        




