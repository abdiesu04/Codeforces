from collections import defaultdict


t =int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    mapp = defaultdict(int)
    for i in range(n):
        mapp[arr[i]] += 1
    ans  = 0
    for i in mapp.values():
        if i == 2:
            ans += 1
    print(ans)