t = int(input())
parent = [n for n in range(t + 1)]
res = [[n] for n in range(t + 1)]
size = [1 for _ in range(t + 1)]
def find(x):
    while x != parent[x]:
        x = parent[x]
    return x

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return 
    if size[y] > size[x]:
        x , y = y , x
    parent[y] = x
    size[x] +=size[y]
    res[x].extend(res[y])

for _ in range(t- 1):
    u, v = map(int, input().split())
    union(u, v)
# print(res)
for i in res:
    if len(i) == t:
        print(*i)
        break
