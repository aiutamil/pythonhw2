arr = input("Enter array:")
list_new = list(map(int, arr.split()))

sum = 0
for i in range(len(list_new)):
    if list_new[i] > 5:
        sum += list_new[i]
print("Sum:",sum)
