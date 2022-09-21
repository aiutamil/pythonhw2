x=[]
c=int(input('Enter number of elements:'))
x=[ int(input('Enter elements:')) for i in range (0, c) ]
max_x = max(x)
print('Maximum element:', max_x)
res=x[::-1]
print('Array in reverse order:', res)
