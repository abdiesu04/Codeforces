class DisjointSets:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)
    
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        
        if x_root != y_root:
            if self.rank[x_root] < self.rank[y_root]:
                self.parent[x_root] = y_root
            elif self.rank[x_root] > self.rank[y_root]:
                self.parent[y_root] = x_root
            else:
                self.parent[y_root] = x_root
                self.rank[x_root] += 1
    
    def same_set(self, x, y):
        return self.find(x) == self.find(y)


n, m = map(int, input().split())
dsu = DisjointSets(n)

for _ in range(m):
    query, u, v = input().split()
    u = int(u)
    v = int(v)
    
    if query == "union":
        dsu.union(u, v)
    elif query == "get":
        if dsu.same_set(u, v):
            print("YES")
        else:
            print("NO")