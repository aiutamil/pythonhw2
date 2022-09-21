import numpy

a = input("Enter numbers:")
list_new = list(map(float, a.split()))

mean_list = list_new
mean = numpy.mean(mean_list)

for i in range(len(list_new)):
    if mean_list[i] == 0:
        mean_list[i] = mean

print("array if replace 0 with mean", mean_list)
