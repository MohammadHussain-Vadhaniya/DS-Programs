SIZE = 5
queue = [] * SIZE
front = -1
rear = -1

def isFull():
    return (rear + 1) % SIZE == front

def isEmpty():
    return front == -1

while True:
    print("\n--- Toll Plaza Simulation ---")
    print("1. Vehicle Arrives")
    print("2. Vehicle Leaves")
    print("3. Display Queue")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        if isFull():
            print("Toll Plaza Full! Vehicle must wait.")
        else:
            vehicle = input("Enter Vehicle Number: ")

            if front == -1:
                front = rear = 0
            else:
                rear = (rear + 1) % SIZE

            queue[rear] = vehicle
            print("Vehicle Entered.")

    elif choice == 2:
        if isEmpty():
            print("No Vehicle in Queue.")
        else:
            print("Vehicle Left:", queue[front])

            if front == rear:
                front = rear = -1
            else:
                front = (front + 1) % SIZE

    elif choice == 3:
        if isEmpty():
            print("Queue Empty")
        else:
            print("Vehicles in Queue:")
            i = front
            while True:
                print(queue[i])
                if i == rear:
                    break
                i = (i + 1) % SIZE

    elif choice == 4:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice")
