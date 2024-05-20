t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    s = a + b + c 
    ans = min(s // 2, a + b)
    if s % 2 != 0:
        print(-1)
    else:
        print(ans)
