numbers= []
while True:
    number= input("Enter the number: ")
    if number =="":
        break
    numbers.append(int(number))
numbers.sort(reverse=True)
print("five greatest numbers", numbers[:5])


