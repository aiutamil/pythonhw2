arr = input("Enter array:")
list_new = list(map(float, arr.split()))

largNumb = False
list_new.sort(reverse=True)

for i in reversed(list_new):
    if i%2 != 0:
        print(i)
        break
