from math import ceil

t = int(input())
for _ in range(t):
    n, h = map(int, input().split())
    d = list(map(int, input().split()))
    t = list(map(int, input().split()))
    l, r = 1, max(d)
    result = -1

    while l <= r:
        mid = l + (r - l) // 2
        tm = 0
        for i in range(len(d)):
            tm += ceil(d[i] / mid) * t[i]
        if tm <= h:
            result = mid
            r = mid - 1
        else:
            l = mid + 1

    print(result)