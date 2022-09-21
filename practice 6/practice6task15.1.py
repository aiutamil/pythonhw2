arr = input("Enter array:")
list_new = list(map(int, arr.split()))

absence = True
for i in range(len(list_new)):
    for l in range(i + 1, len(list_new)):
        if list_new[i] == list_new[l]:
            absence = False
            print("Duplicates:", list_new[i], "and indices (", i,",", l, ")")
if absence == True: print("No dublicates")
