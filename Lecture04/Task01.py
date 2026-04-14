import random
number= int(input("How many dice do you want to roll:  "))
total = 0
for i in range(number):
    dice = random.randint(1, 6)
    print("Dice", i + 1, ":", dice)
    total += dice
print("Total dice:", total)