import random
def roll_dice():
    return random.randint(1, 6)

while True:
    num = roll_dice()
    print(num)

    if num == 6:
        break