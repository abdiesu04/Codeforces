
from collections import defaultdict


n = int(input())
tree = list(map(int, input().split()))
colors = list(map(int, input().split()))
adj = defaultdict(list)
for i in range(1, n):
    adj[tree[i - 1] - 1].append(i)

visited = set()
steps = 0

# def dfs(node, color):
#     if node in visited:
#         return
#     visited.add(node)
#     global steps
#     if colors[node] != color:
#         steps += 1
#         color = colors[node]
#     for child in adj[node]:
        
#         dfs(child, color)
#     return steps

def dfs(node, color):
    stack = [(node, color)]
    while stack:
        node, color = stack.pop()
        if node not in visited:
            visited.add(node)
            global steps
            if colors[node] != color:
                steps += 1
                color = colors[node]
            for child in adj[node]:
                stack.append((child, color))
    return steps
print(dfs(0, 0))
