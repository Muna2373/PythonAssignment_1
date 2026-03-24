#Assignment 02:
#Write a program that asks the user for the radius of a circle and then prints out the area with two decimals
#of the circle.


radius=float(input("Enter the radius of a circle: "))
area= 3.14159* radius* radius
print(f" Area of the circle is {area:.2f}")   #.2f-> show only 2 decimal places
