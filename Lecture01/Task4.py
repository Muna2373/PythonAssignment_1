#Assignment 04:
#Write a program that asks the user for three integer numbers. The program prints out the sum, product, and average
#of the numbers.



Number1= int(input("Enter the first number: "))
Number2= int(input("Enter the second number: "))
Number3= int(input("Enter the third number: "))
sum= Number1+Number2+Number3
product= Number1*Number2*Number3
average=  sum/3
print(f"Sum:{sum}")
print(f"Product:{product}")
print(f"Average:{average}")
