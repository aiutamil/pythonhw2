import itertools
s = input("Enter array:")
list_new = list(map(float, s.split()))

result = sum(itertools.islice(list_new, 0,len(list_new),2))

print("Array:", list_new)
print("Sum of odd elements:", result)
