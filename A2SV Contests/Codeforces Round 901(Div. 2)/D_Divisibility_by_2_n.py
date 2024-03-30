t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int , input().split()))
    ans = 0
    product = 1
    for i in arr:
        product *= i
    p = 1
    for i in range(1, n +1):
        p *= i
    if (product * p) % 2**n != 0:
        ans = -1
        
        
    elif product % 2**n == 0:
        ans = 0
    
    else:
        
        d = 0
        while d != n:
            if product % 2 == 0:
                product //= 2
                d += 1
            else:
                product *= (n- d) * 2
                ans += 1
                product //= 2
                d += 1
        
        

    print(ans )

