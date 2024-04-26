def dfs(v):
    stack = [v]
    used[v] = 1
    while stack:
        node = stack[-1]
        done = True
        for to in g[node]:
            if not used[to]:
                used[to] = 1
                stack.append(to)
                done = False
                break
        if done:
            ord.append(stack.pop())


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    edges = []
    for _ in range(m):
        t, x, y = map(int, input().split())
        x, y = x - 1, y - 1
        if t == 1:
            g[x].append(y)
        edges.append((x, y))

    ord = []
    used = [0] * n
    for i in range(n):
        if not used[i]:
            dfs(i)

    pos = [0] * n
    ord.reverse()
    for i in range(n):
        pos[ord[i]] = i

    bad = False
    for i in range(n):
        for j in g[i]:
            if pos[i] > pos[j]:
                bad = True

    if bad:
        print("NO")
    else:
        print("YES")
        for x, y in edges:
            if pos[x] < pos[y]:
                print(x + 1, y + 1)
            else:
                print(y + 1, x + 1)


