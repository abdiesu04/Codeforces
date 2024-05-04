t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = set(a)
    v = list(s)
    if len(s) % 2 != 0 or v[0] != 1:
        print("Alice")
    else:
        print("Bob")