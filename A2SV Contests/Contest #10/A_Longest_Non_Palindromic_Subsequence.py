from collections import defaultdict


t = int(input())
for _ in range(t):
    s = input()
    last = defaultdict(int)
    for i in range(len(s)) :
        last[s[i]] = i
    ans = -1
    for i in range(len(s)):
        ans = max(abs(i - last[s[i]]), ans)
    print(-1 if len(set(s)) == 1 else ans)     