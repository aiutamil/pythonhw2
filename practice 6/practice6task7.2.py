arr = input("Enter array:")
list_new = list(map(int, arr.split()))

max = list_new[0]
maxID = 0
for i in range(len(list_new)):
    if list_new[i] > max:
        max = list_new[i]
        maxID = i

min = list_new[0]
minID = 0
for l in range(len(list_new)):
    if list_new[l] < min:
        min = list_new[l]
        minID = l

print("Maximum value:",max)
print("Minimum value:",min)
list_new[minID] = max
list_new[maxID] = min
print("Swapped array:",list_new)
