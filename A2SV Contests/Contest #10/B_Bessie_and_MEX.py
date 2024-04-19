

t = int(input())

for I in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    perm = [0] * n
    mex = n
    for i in range(n - 1, -1, -1):
        if a[i] > 0:
            perm[i] = mex - a[i]
            mex = perm[i]
        else:
            perm[i] = mex + abs(a[i])
    print(*perm)
   