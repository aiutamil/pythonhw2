arr = input("Enter array:")
list_new = list(map(int, arr.split()))

sum = 0
product = 1
for i in range(len(list_new)):
    if list_new[i] % 2 == 0:
        sum += list_new[i]
    if list_new[i] % 2 != 0:
       product *= list_new[i]

print("Sum of numbers:",sum)
print("Product of numbers:",product)
