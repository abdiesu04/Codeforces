def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    m = {}
    for i in a:
        if i in m:
            m[i] += 1
        else:
            m[i] = 1
    flag = 0
    print(m)
    for e in m.values():
        if e >= k:
            flag = 1
    if flag == 0:
        print(n)
    else:
        print(k-1)

T = int(input())
for _ in range(T):
    solve()