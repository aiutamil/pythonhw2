arr = input("Enter array:")
list_new = list(map(int, arr.split()))

list_new = list(dict.fromkeys(list_new))
print(list_new)
