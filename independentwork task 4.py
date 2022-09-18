a=[]
n= int(input("Enter the number of elements in list:"))
for x in range(0,n):
    element=int(input("Enter element " + str(x+1) + ":"))
    a.append(element)
temp=a[0]
a.sort()
print ("Largest element is:", a[-1])
b=int(a[-1]/n)
print (b)
