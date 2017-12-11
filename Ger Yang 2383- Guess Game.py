import random
num = (random.randint(1, 50))

guesses = 0

print("Welcome to the guessing game.")
print("The computer guesses a number from 1 to 50.")
print("The user will guess the number.")
print("Ready, begin...")

while guesses < 5:
    guess = input(" ")
    guess = int(guess)

    guesses = guesses + 1

    if guess > num:
        print("You guess too high, guess a little lower.")

    if guess < num:
        print("Too low, guess higher.")

if num == num:
    guess = num
    print("You got it correct.")

if num != num:
    guess = num
    print("You lost, the number I was thinking was %s." % random.randint(1, 50))
