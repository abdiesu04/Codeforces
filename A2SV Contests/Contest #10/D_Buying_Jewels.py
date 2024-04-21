t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())
    arr = list(map(int, input().split()))
    vp = [(arr[i], i) for i in range(n)]
    vp.sort()

    q = [0] * n
    for i in range(len(vp)):
        if k > 0:
            q[vp[i][1]] = min(m, k)
            k -= min(m, k)

    ans = 0
    extra = 0
    for i in range(n):
        ans += q[i] * (arr[i] + extra)
        extra += q[i]

    print(ans)