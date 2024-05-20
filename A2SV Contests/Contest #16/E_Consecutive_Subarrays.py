n, k = map(int, input().split())
a = list(map(int, input().split()))

sum = 0
v = []
for i in range(n - 1, -1, -1):
    sum += a[i]
    if i > 0:
        v.append(sum)
res = sum
v.sort(reverse=True)
# print(v)

for i in range(k - 1):
    res += v[i]
    # print(v[i])

print(res)