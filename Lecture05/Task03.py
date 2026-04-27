airports = {}
while True:
    print("\n1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")

    choice = input("Choose an option from 1 to 3: ")

    if choice == "1":
        code = input("Enter ICAO code: ")
        name = input("Enter airport name: ")
        airports[code] = name
        print("Airport saved")

    elif choice == "2":
        code = input("Enter ICAO code: ")
        if code in airports:
            print(airports[code])
        else:
            print("Airport is not found")
    elif choice == "3":
        print("Goodbye")
        break
    else:
        print("Invalid choice")