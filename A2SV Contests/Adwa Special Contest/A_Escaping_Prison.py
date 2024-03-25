t = int(input())
for _ in range(t):
    n , h = map(int, input().split())
    sm = 0
    for _ in range(n):
        w, l = map(int, input().split())
        sm += max(w , l)
    if h <= sm:
        print("YES")
    else:
        print("NO")