#Assignment 06:

#Write a program that generates two random combinations of numbers for a combination lock:
#A3-digit code where each number is between 0 and 9.
#A4-digit code where each number is between 1 and 6.

import random
digit1= random.randint(0,9)
digit2= random.randint(0,9)
digit3= random.randint(0,9)
print(f"3-digit code (0-9):",digit1, digit2,digit3)


digit4= random.randint(0,6)
digit5= random.randint(0,6)
digit6= random.randint(0,6)
digit7= random.randint(0,6)
print(f"4-digit code(0-6):", digit4, digit5, digit6, digit7)