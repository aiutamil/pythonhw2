s = str(input('Enter string:'))
news = ''
for i in s.split():
    if i.endswith('i'):
        print(i, " ")
