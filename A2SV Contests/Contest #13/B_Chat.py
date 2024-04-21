



import heapq
n,k , q = map(int,input().split())
t = list(map(int,input().split()))
a = []
for _ in range(q):
    x,y = map(int,input().split())
    if x == 1:
        a.append(t[y-1])
        if len(a) > k:
            a.remove(min(a))
    else:
        if t[y-1] in a:
            print('YES')
        else:
            print('NO')