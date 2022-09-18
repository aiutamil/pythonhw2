a=[]
n= int(input("Enter the number of elements in list:"))
for x in range(0,n):
    element=input("Enter parameter " + str(x+1) + ":")
    a.append(element)
temp=a[0]
print("New list is:")
print(a)
