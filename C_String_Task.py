s  = input()
res = []
for i in s:
    if i not in "AEIOYyUaeiou" and not i.isupper():
        res.append('.')
        res.append(i)
    elif i not in "AEYyIOUaeiou" and i.isupper():
        res.append('.')
        res.append(i.lower())
print(''.join(res))

