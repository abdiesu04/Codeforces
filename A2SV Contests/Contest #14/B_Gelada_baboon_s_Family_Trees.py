
n = int(input())

parent = [n for n in range(n+1)]

def find(x):
    while x != parent[x]:
        x = parent[x]
    return x

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x

p = list(map(int, input().split()))
for i in range(n):
    union(i+1, p[i])
print(len(set(find(i+1) for i in range(n))))

