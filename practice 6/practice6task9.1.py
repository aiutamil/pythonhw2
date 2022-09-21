arr = input("Enter array:")
list_new = list(map(float, arr.split()))

min = abs(list_new[0])
minID = 0

for i in range(len(list_new)):
    if abs(list_new[i]) <= min:
        min = abs(list_new[i])
        minID = i

print("Minimum element in array:", list_new[minID])
list_new.reverse()

print("Array in reverse order: ", list_new)
