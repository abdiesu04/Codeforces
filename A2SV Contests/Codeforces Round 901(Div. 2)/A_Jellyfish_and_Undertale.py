t = int(input())

for _ in range(t):
    a, b, n = map(int, input().split())
    arr = list(map(int,input().split()))
    ans = b

    for i in arr:
        ans += min(a - 1, i)

    print(ans)