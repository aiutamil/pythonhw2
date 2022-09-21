arr = input("Enter array:")
list_new = list(map(int, arr.split()))

list_new11 = []

for i in list_new:
    if i < 10:
        if i % 2 == 0:
            list_new11.append(i)

if len(list_new11) == 0: print("No such numbers")
else:print(list_new11)
