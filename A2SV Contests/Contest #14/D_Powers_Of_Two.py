from collections import deque

n, k = map(int, input().split())

ans = {}
q = deque()

for i in range(31):
    if n & (1 << i):
        if i > 0:
            q.append(1 << i)
        ans[1 << i] = ans.get(1 << i, 0) + 1

if len(ans) > k:
    print("NO")
    exit(0)

cnt = len(ans)

while cnt < k and q:
    z = q.popleft()
    ans[z] -= 1
    ans[z // 2] = ans.get(z // 2, 0) + 2
    if z // 2 > 1:
        q.append(z // 2)
        q.append(z // 2)
    cnt += 1

if cnt < k:
    print("NO")
else:
    print("YES")
    for x in ans:
        for i in range(ans[x]):
            print(x, end=" ")
    print()