arr = input("Enter array:")
list_new = list(map(float, arr.split()))

print("Original array:",list_new)

for i in range(len(list_new)):
    if list_new[i] < 10 :
        list_new[i] = 0
    elif list_new[i] > 20:
        list_new[i] = 1

print("Changed array:",list_new)
