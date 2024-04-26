# B. Disjoint Sets Union 2
# time limit per test1 second
# memory limit per test256 megabytes
# inputstandard input
# outputstandard output
# Implement disjoint sets union data structure. You have to perform queries of two types:

# union u
#  v
#  — unite two sets that contain u
#  and v
# , respectively;
# get v
#  — find the set to which v
#  belongs to, find the minimal and the maximal element of the set, and the total number of elements in it.
# Input
# The first line of the input contains two integers n
#  and m
#  (1≤n,m≤3⋅105
# ) — the number of elements and the number of queries. Next m
#  lines contain queries, one per line. For a query union the line looks like union u
#  v
#  (1≤u,v≤n
# ). For a query get the line looks like get v
#  (1≤v≤n
# ).

# Output
# For each operation get you should output the result on a separate line in the respected order. Each result should consist of three integers: the minimal element, the maximal element and the number of elements in the set.

# Example
# inputCopy
# 5 11
# union 1 2
# get 3
# get 2
# union 2 3
# get 2
# union 1 3
# get 5
# union 4 5
# get 5
# union 4 1
# get 5
# outputCopy
# 3 3 1
# 1 2 2
# 1 3 3
# 5 5 1
# 4 5 2
# 1 5 5











class Disjoint:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)
        self.min = [0] * (n + 1)
        self.max = [0] * (n + 1)
        self.size = [1] * (n + 1)
        for i in range(1, n + 1):
            self.min[i] = i
            self.max[i] = i

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root != y_root:
            if self.rank[x_root] < self.rank[y_root]:
                x_root, y_root = y_root, x_root
            # self.parent[y_root] = x_root
            # self.size[x_root] += self.size[y_root]
            # self.min[x_root] = min(self.min[x_root], self.min[y_root])
            # self.max[x_root] = max(self.max[x_root], self.max[y_root])
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[x_root] += 1

    def get(self, x):
        x_root = self.find(x)
        return self.min[x_root], self.max[x_root], self.size[x_root]
    
n , t = input().split()
n = int(n)
t = int(t)
dsu = Disjoint(n)
for _ in range(t):
    query, *args = input().split()
    if query == "union":
        u, v = map(int, args)
        dsu.union(u, v)
    elif query == "get":
        v = int(args[0])
        print(*dsu.get(v))
    
