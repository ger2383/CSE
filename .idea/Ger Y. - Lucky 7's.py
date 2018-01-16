import random
money_left = 15

while money_left > 0:
    Dice1 = random.randint(1, 6)
    Dice2 = random.randint(1, 6)
    total = Dice1 + Dice2
    print(total)

    if total == 7:
        print("You Win")
    elif total > 7:
        print("You Lose")
        money_left -= 1
    elif total < 7:
        print("You Lose")
        money_left += 1

