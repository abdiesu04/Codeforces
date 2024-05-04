t = int(input())

for _ in range(t):
    n = int(input())
    x = list(map(int, input().split()))

    a = [0] * n

    max_value = max(x)
    a[0] = max_value + 1
   
    for i in range(1, n):
        a[i] = x[i-1] + a[i-1]
        
    print(*a)