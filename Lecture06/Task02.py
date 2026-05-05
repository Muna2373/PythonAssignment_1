def gallons_to_litres(gallons):
    litres = gallons * 3.785
    return litres

while True:
    gallons = float(input("Enter gallons: "))
    if gallons < 0:
        print("Program ended.")
        break

    litres = gallons_to_litres(gallons)
    print("Litres:", litres)