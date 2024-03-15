t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    if n > len(s):
        print(s + s[::-1] * ((n - len(s)) // 2))
    else:
        print(s + s[::-1][:n//2])