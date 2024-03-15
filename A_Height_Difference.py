t = int(input())
for i in range(t):
    n , x = map(int,input().split())
    flaag = True
    nums = list(map(int , input().split()))
    nums.sort()
    for i in range(n):
        # print(i , i + n -1)
        if nums[i + n ] - nums[i] < x:  
            flaag = False
    print("YES" if flaag else "NO")
            