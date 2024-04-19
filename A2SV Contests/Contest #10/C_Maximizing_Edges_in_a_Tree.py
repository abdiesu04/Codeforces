from collections import defaultdict
# maximum number of edges you can add to make the graph bipartite
n = int(input())
res = 0
graph = defaultdict(list)
for _ in range(n-1):
    a, b = map(int, input().split())
    
    graph[a].append(b)
    graph[b].append(a)
visited = set()
colors = [-1 for _ in range(n+1)]
col = 1
def dfs(node):
    col  = - col
    visited.add(node)
    for child in graph[node]:
        if child not in visited and col:
            res += 1
            dfs(child)
dfs(1)

print(res)
