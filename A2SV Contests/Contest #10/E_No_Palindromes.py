t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    zeus = list(map(int, input().split()))

    max_val = max(zeus)
    max_count = zeus.count(max_val)

    ans1 = 0
    for i in range(k):
        if zeus[i] == max_val:
            ans1 += 1

    ans2 = 0
    for i in range(n):
        if zeus[i] > max_val or (zeus[i] == max_val and i < k):
            ans2 += 1

    print(max(ans1, ans2))