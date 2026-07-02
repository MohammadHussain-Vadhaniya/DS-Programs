# Linear Search - Spam Detector

blacklist = [
    "spam123@gmail.com",
    "fake@mail.com",
    "abc@yahoo.com",
    "test@spam.com"
]

email = input("Enter sender email: ")

found = False

for sender in blacklist:
    if sender == email:
        found = True
        break

if found:
    print("Spam Email Detected!")
else:
    print("Safe Email")
