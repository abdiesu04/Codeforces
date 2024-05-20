
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
    
