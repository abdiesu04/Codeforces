t = int(input())  

while t > 0:
    n, x, k = map(int, input().split()) 

    if 2 * k >= x * (x + 1) and 2 * k <= n * (n + 1) - (n - x) * (n - x + 1):
        print("YES")
    else:
        print("NO")

    t -= 1