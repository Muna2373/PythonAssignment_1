minimum_size= 42

length=float(input("Enter the length of a zander in centimeter: "))

if length < minimum_size:
    print("You must release this zander back into the lake.")
    difference = minimum_size - length
    print(f" It is {difference}cm short from the legal minimum size of {minimum_size}cm.")
else:
    print(f" You can keep it.")




