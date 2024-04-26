class DSU:
    def __init__(self, n):
        self.par = list(range(n + 1))
        self.exp = [0] * (n + 1)
        self.sizz = [1] * (n + 1)

    def find_set(self, s):
        if self.par[s] == s:
            return (s, self.exp[s])
        parent, parent_exp = self.find_set(self.par[s])
        self.par[s] = parent
        self.exp[s] += parent_exp - self.exp[parent]
        return (self.par[s], self.exp[s] + self.exp[self.par[s]])

    def union_set(self, u, v):
        u = self.find_set(u)[0]
        v = self.find_set(v)[0]
        if u == v:
            return
        if self.sizz[u] > self.sizz[v]:
            u, v = v, u
        self.par[u] = v
        self.exp[u] -= self.exp[v]
        self.sizz[v] += self.sizz[u]

    def add_experience(self, x, v):
        x = self.find_set(x)[0]
        self.exp[x] += v


n, m = map(int, input().split())
gr = DSU(n)

for _ in range(m):
    query, *args = input().split()

    if query == "join":
        x, y = map(int, args)
        gr.union_set(x, y)
    elif query == "add":
        x, v = map(int, args)
        gr.add_experience(x, v)
    else:
        x = int(args[0])
        print(gr.find_set(x)[1])