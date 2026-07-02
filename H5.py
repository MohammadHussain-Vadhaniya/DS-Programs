# Binary Search - First Price >= Target

prices = [20000, 30000, 40000, 55000, 58000, 64000, 73000]

target = int(input("Enter minimum price: "))

low = 0
high = len(prices) - 1
answer = -1

while low <= high:
    mid = (low + high) // 2

    if prices[mid] >= target:
        answer = mid
        high = mid - 1
    else:
        low = mid + 1

if answer != -1:
    print("First price >= target is:", prices[answer])
else:
    print("No product found.")
