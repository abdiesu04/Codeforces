from collections import deque

def isok(x, y):
    return 0 <= x < 2 and 0 <= y < n

def solve():
    q = deque()
    q.append([0, 0])
    l1 = [[0 for _ in range(n)] for _ in range(2)]
    l1[0][0] = 1
    while q:
        x, y = q.popleft()
        if x == 1 and y == n - 1:
            return "YES"
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if isok(nx, ny):
                if l[nx][ny] == "<":
                    ny -= 1
                else:
                    ny += 1
                if l1[nx][ny] == 1:
                    continue
                l1[nx][ny] = 1
                q.append((nx, ny))
    return "NO"

t = int(input())
for _ in range(t):
    n = int(input())
    l = []
    l.append(input())
    l.append(input())
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    result = solve()
    print(result)