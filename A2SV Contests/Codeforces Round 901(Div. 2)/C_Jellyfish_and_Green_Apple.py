import math

def solve():
    n, m = map(int, input().split())
    n %= m
    a = n // math.gcd(n, m)
    b = m // math.gcd(n, m)
    if bin(b).count('1') > 1:
        print("-1")
    else:
        print((bin(a).count('1')) * m - n)

T = int(input())

for _ in range(T):
    solve()