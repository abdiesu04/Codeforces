def solve():
    n, a, b = map(int, input().split())
    total = (n // 2) * min(2 * a, b) + (n % 2) * a
    print(total)

t = int(input())
for _ in range(t):
    solve()