t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[1] != a[0]:
        print("YES")
    else:
        flag = False
        for i in range(1 , n):
            if a[i] % a[0] != 0:
                flag = True 
                break
        print("YES" if flag else "NO")
