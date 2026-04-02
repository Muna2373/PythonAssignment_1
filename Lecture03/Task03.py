
numbers = []
while True:
    entry = input("Enter a number : ")
    if entry == "":
        break
    numbers.append(float(entry))
print("Smallest number:", min(numbers))
print("Largest number:", max(numbers))