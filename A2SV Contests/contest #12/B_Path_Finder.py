from collections import defaultdict

n = int(input())
graph = defaultdict(list)
for i in range(n - 1):
    u, v, c = map(int, input().split())
    graph[u].append((v, c))
    graph[v].append((u, c))

def dfs(node, parent, dist):
    global max_dist
    max_dist = max(max_dist, dist)
    for neighbor, c in graph[node]:
        if neighbor != parent:
            dfs(neighbor, node, dist + c)
    return max_dist

max_dist = 0
print(dfs(0, -1, 0))
