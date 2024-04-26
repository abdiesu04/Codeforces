n = int(input())

graph = {}
cant_start = set()

for _ in range(n):
    old, new = input().split()
    graph[old] = new
    cant_start.add(new)

ans = []

for old, new in graph.items():
    if old in cant_start:
        continue
    cur = old

    while cur in graph:
        cur = graph[cur]

    ans.append((old, cur))

print(len(ans))
for old, new in ans:
    print(old , new)