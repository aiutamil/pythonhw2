arr = input("Enter array:")
list_new = list(map(int, arr.split()))

list_odd = []

for i in range(len(list_new)):
    if list_new[i] % 2 != 0:
        list_odd.append(list_new[i])
list_odd.sort(reverse=True)

if len(list_odd)==0:
    print("No odd numbers")
else:
    print("Odd array: ", list_odd)
