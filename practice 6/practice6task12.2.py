arr1 = input("Enter first array: ")
list_new1 = list(map(float, arr1.split()))

arr2 = input("Enter second array: ")
list_new2 = list(map(float, arr2.split()))

list_new2,list_new1 = list_new1,list_new2

print("First array:",list_new1)
print("Second array:",list_new2)
