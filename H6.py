# Merge Two Sorted Lists

list1 = [3, 6, 7, 13]
list2 = [1, 5, 8, 10]

merged = []

i = 0
j = 0

while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
        merged.append(list1[i])
        i += 1
    else:
        merged.append(list2[j])
        j += 1

while i < len(list1):
    merged.append(list1[i])
    i += 1

while j < len(list2):
    merged.append(list2[j])
    j += 1

print("Merged Waitlist:")
print(merged)
