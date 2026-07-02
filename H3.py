backStack = []
forwardStack = []
current = "Home"

while True:
    print("\nCurrent Location:", current)
    print("1. Visit New Place")
    print("2. Go Back")
    print("3. Go Forward")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        place = input("Enter New Place: ")
        backStack.append(current)
        current = place
        forwardStack.clear()

    elif choice == 2:
        if backStack:
            forwardStack.append(current)
            current = backStack.pop()
        else:
            print("No Previous Place!")

    elif choice == 3:
        if forwardStack:
            backStack.append(current)
            current = forwardStack.pop()
        else:
            print("No Forward Place!")

    elif choice == 4:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice")
