from collections import Counter

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    s = Counter(a)
    i = j = answer = 0
    while j < n:
        if a[i] > b[j]:
            s[a[i]] -= 1
            if s[a[i]] == 0:
                del s[a[i]]
            s[b[j]] += 1
            answer += 1
            j += 1
        else:
            i += 1
            j += 1
    print(answer)

t = int(input())
for _ in range(t):
    solve()