
from collections import defaultdict


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))

  





def find(parent, node):
    if parent[node] == node:
        return node
    parent[node] = find(parent, parent[node])
    return parent[node]

def union(parent, rank, x, y):
    x_parent = find(parent, x)
    y_parent = find(parent, y)
    if rank[x_parent] < rank[y_parent]:
        parent[x_parent] = y_parent
    elif rank[x_parent] > rank[y_parent]:
        parent[y_parent] = x_parent
    else:
        parent[y_parent] = x_parent
        rank[x_parent] += 1

def find_minimum_cycle(n, edges):
    parent = [i for i in range(n+1)]
    rank = [0] * (n+1)
    graph = defaultdict(list)
    last_edge = None

    edges.sort(key=lambda x: x[2], reverse=True)

    for u, v, w in edges:
        parent_u = find(parent, u)
        parent_v = find(parent, v)

        if parent_u != parent_v:
            union(parent, rank, parent_u, parent_v)
            graph[u].append((v, w))
            graph[v].append((u, w))
        else:
            last_edge = (u, v, w)

    start, end, _ = last_edge
    path = []
    visited = set()

 
