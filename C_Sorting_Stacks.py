t = int(input())
for _ in range(t):
    n = int(input())
    height = [int(x) for x in input().split()]
    height_sum = 0
    for i in range(n):
        height_sum += height[i]
        if height_sum < i*(i+1)//2:
            print("NO")
            break
    else:
        print("YES")

