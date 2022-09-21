a = input("Enter numbers:")
list_new = list(map(int, a.split()))

list_positive = []
list_negative = []

for i in range(len(list_new)):
    if list_new[i] <= 0:
        list_negative.append(list_new[i])
    else:
        list_positive.append((list_new[i]))

print("2nd array: ",list_positive)
print("3th array: ",list_negative)
