t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    cnt = [0] * 31
    a = list(map(int, input().split()))
    for i in range(n):
        for j in range(31, -1, -1):
            if a[i] & (1 << j):
                cnt[j] += 1
    ans = 0
    for i in range(30, -1, -1):
        need = n - cnt[i]
        if need <= k:
            k -= need
            ans += (1 << i)
    print(ans)