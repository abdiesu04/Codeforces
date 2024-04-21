

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = ''
    for i in range(k):
        s += chr(ord('a') + i) * (n // k)
    s += chr(ord('a') + k - 1) * (n % k)
    print(s)