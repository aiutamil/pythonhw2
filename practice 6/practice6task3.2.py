arr = input("Enter array:")
list_new = list(map(int, arr.split()))

for i in range(len(list_new)):
    if list_new[i] < 15:
        list_new[i] = list_new[i] * 2
print("Final array:", list_new)
