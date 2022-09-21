import numpy
arr = input("Enter array:")
list_new = list(map(int, arr.split()))

mean = numpy.mean(list_new)

for i in range(len(list_new)):
    if list_new[i] == 0:
        list_new[i] = mean

print("Result:",list_new)
