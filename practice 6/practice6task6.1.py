arr = input("Enter array:")
list_new = list(map(int, arr.split()))

list_new.sort()
print("Maximum number in array:", list_new[len(list_new)-1])

list_new.sort(reverse=True)
print("Minimum number in array:", list_new[len(list_new)-1])
