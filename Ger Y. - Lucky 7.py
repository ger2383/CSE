import random
money_left = 15
plays = 0

while money_left > 0:
    Dice1 = random.randint(1, 6)
    Dice2 = random.randint(1, 6)
    total = Dice1 + Dice2

    if total == 7:
        print("You Win, + $4")
        money_left += 4
        plays += 1
        print("You have $%s" % money_left)
    elif total > 7:
        print("You Lose, - $1")
        money_left -= 1
        plays += 1
        print("You have $%s" % money_left)
    elif total < 7:
        print("You Lose, - $1")
        money_left -= 1
        plays += 1
        print("You have $%s" % money_left)
    elif money_left == 0:
        print("You played %s rounds" % plays)




