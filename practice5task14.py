s=str(input('Enter string:'))
news = ''
for i in s.split():
    if i.endswith('i'):
        print(i, " ")


for h in s.split():
    if h.startswith('a'):
        print(h, " ")
