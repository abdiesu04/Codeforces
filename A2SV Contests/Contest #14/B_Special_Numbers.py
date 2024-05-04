t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    res = 0

    for i in range(32):
        if k & (1 << i):
            res += pow(n, i, 10**9 + 7)
            res %= 10**9 + 7

    print(res)