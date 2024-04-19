import sys

I, i, j, k, l, a, b, c, x, y = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
ll_MAX = sys.maxsize
ll_MIN = -sys.maxsize - 1

t = int(input())

for I in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    element = 0
    p = [0] * n
    current_mex = n
    for i in range(n - 1, -1, -1):
        if a[i] > 0:
            p[i] = current_mex - a[i]
            current_mex = p[i]
        else:
            p[i] = current_mex + abs(a[i])
    for i in range(n):
        print(p[i], end=" ")
    print()