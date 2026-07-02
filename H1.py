belt = [] * 8

while True:
    print("\n--- Amazon Fulfillment Centre ---")
    print("1. Add Product")
    print("2. Check Product at Slot")
    print("3. Find Product")
    print("4. Check if Belt is Full")
    print("5. Display Belt")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        slot = int(input("Enter slot (0-7): "))
        if 0 <= slot < 8:
            product = input("Enter product name: ")
            belt[slot] = product
            print("Product stored successfully.")
        else:
            print("Invalid slot!")

    elif choice == 2:
        slot = int(input("Enter slot (0-7): "))
        if 0 <= slot < 8:
            print("Product:", belt[slot])
        else:
            print("Invalid slot!")

    elif choice == 3:
        product = input("Enter product to search: ")
        if product in belt:
            print("Found at slot:", belt.index(product))
        else:
            print("Product not found.")

    elif choice == 4:
        if None not in belt:
            print("Conveyor Belt is FULL.")
        else:
            print("Conveyor Belt is NOT FULL.")

    elif choice == 5:
        for i in range(8):
            print(f"Slot {i}: {belt[i]}")

    elif choice == 6:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!")
