s=input('Enter string:')
n=len(s)
s = s[:n // 2].replace('n', '*') + s[n // 2:]
print(s)
