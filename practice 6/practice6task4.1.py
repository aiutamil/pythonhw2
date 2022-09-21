arr = input("Enter array:")
list_new = list(map(int, arr.split()))

max = list_new[0]
maxID = 0
for i in range(len(list_new)):
    if list_new[i] >= max:
        max = list_new[i]
        maxID = i

print("Maximum number in array:", max)
print("Ordinal number for him",end=" ")

if maxID == 0: print("First:")
elif maxID == 1:print("Second:")
elif maxID == 2:print("Third:")
else: print('{}th'.format(maxID+1))
