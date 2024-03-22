n = input()
s = input()
n = int(n)
if n == 1:
    print(s)
    exit()
div = []
for i in range(1 , n+1):
    if n % i == 0:
        div.append(i)
for i in div:
    s = s[:i][::-1] + s[i:]
print(s)

# for i in range(n, 1 , n //2):
#     print(s)

