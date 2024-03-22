t = int(input())
for i in range(t):
    n , left = map(int , input().split())
    arr = list(map(int , input().split()))
    mp =  1
    for i in arr:
        mp *= i
    if 2023 % mp == 0:
        print("YES") 
        res = [1] * (left -1)
        res.append(2023 // mp)
        print(*res)
    else:
        print("NO")
