def fn(a, k):
    n = len(a)
    tmp = [0] * n
    for i in range(n - k + 1):
        cur = a[i]
        ops = 0
        if i > 0:
            ops += tmp[i - 1]
        idx = max(0, i - k + 1)
        if idx > 0:
            ops -= tmp[idx - 1]
        if ops % 2:
            cur = 1 - cur
        if i > 0:
            tmp[i] = tmp[i - 1]
        if cur == 0:
            tmp[i] += 1
    
    for i in range(n - k + 1, n):
        tmp[i] = tmp[i - 1]
        cur = a[i]
        ops = tmp[i - 1]
        idx = max(0, i - k + 1)
        if idx > 0:
            ops -= tmp[idx - 1]
        if ops % 2:
            cur = 1 - cur
        if cur == 0:
            return False
    
    return True

def solve(ttc):
    n = int(input())
    a = [0] * n
    s = input()
    for i in range(n):
        if s[i] == '1':
            a[i] = 1
    
    for k in range(n, 0, -1):
        if fn(a, k):
            print(k)
            return

t = int(input())
for _ in range(t):
    solve(_)