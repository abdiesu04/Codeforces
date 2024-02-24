from collections import defaultdict

t = int(input())
for i in range(t):
    mapp = defaultdict(int)
    n = int(input())
    for i in range(n):
        s = input()
        for j in s:
            mapp[j] += 1
    for w in mapp.values():
        if w % n != 0:
            print("NO")
            break
    else:
        print("YES")