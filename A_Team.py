t = int(input())
cnt = 0
for i in range(t):
    n = list(map (int , input().split()))
    if sum(n) >= 2:
        cnt += 1
print(cnt)