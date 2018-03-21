import random
# This is a guide of how to
# make hangman
#
# 1. Make a word bank - 10 items
# 2. Select a random item to guess
# 3. Take in a letter and add it to a list of letters_guessed
# 4. Reveal Letters based on input
# 5. Create win and lose conditions

word_bank = ["Call of duty 3", "League of Legend", "Hoopa", "Rules of Survival", "Edison High School", "Volleyball",
             "Cincino", "Gallade", "Modern Combat 5", "Killer Instinct"]

word = random.choice(word_bank)
list = word
print(list)

guess = ''
letters_guessed = [' ']
guesses = 10

while guesses > 0:
    output = []
    for letters in word:
        if letters.lower() in letters_guessed:
            output.append(letters)
        else:
            output.append("*")
    print(output)

    guess = input("Guess a letter or The Word: ").lower()
    if guess not in word:
        guesses -= 1
        print("You have %s guess left." % guesses)
    letters_guessed.append(guess)
    print("Letter You Guessed: %s" % guess)
    if guess == word:
        print("Correct")
    if guesses == 0:
        print("You Lose")
print("Good try though")
# L1 = ['h', 'e', 'l', 'l', 'o']
# "".join(L1)