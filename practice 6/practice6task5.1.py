a = int(input("Length of array:"))
arr = input("Enter array:")
list_new = list(map(int, arr.split()))

for i in range(a):
    for l in range(i+1,a):
        if list_new[i] == list_new[l]:
            if list_new[i] < 0 and list_new[l] < 0:
                print(list_new[i], list_new[l])
