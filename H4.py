# Linear Search - Spam Detector

blacklist = [
    "fake123@gmail.com",
    "xzy@mail.com",
    "abc@yahoo.com",
    "valid@spam.com"
]

email = input("Enter sender email: ")

found = False

for sender in blacklist:
    if sender == email:
        found = True
        break

if found:
    print("Fake Email")
else:
    print("Safe Email")
