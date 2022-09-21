import numpy

arr = input("Enter array:")
list_new = list(map(float, arr.split()))

mean = numpy.mean(list_new)

for i in range(len(list_new)):
    if list_new[i] > mean:
        list_new[i] = 1.0
print(list_new)
