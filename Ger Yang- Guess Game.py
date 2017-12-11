import random
# Generate a number
# Ask the user for an input(number)
# Does the guess match the number?
# Add "Higher" and "Lower"
# Add 5 guesses

# Choose a number between 1 and 50
number = (random.randint(1, 50))
guesses = 0

print("Welcome to the guessing game!")
print("The computer guesses a number from 1 to 50 and")
print("the user will guess the number")
print("Ready")
print("Begin")

while guesses < 5:
    guess = input(" ")
    guess = int(guess)

guesses = guesses + 1

if guess < number:
    print("You guess to low guess higher")

if guess > number:
    print("You guess to high guess lower")

    if guess == number:
        break

if guess == number