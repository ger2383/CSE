import random
money_left = 15

while money_left > 0:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    sum = dice1 + dice2

    if sum == 7:
        print("You Won")
        money_left += 5



