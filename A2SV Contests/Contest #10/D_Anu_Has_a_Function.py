n = int(input())
arr =([int(x) for x in input().split()])
arr.sort()

ans = []
l, r = 0, len(arr)-1
while l < r:
    ans.append(arr[r])
    ans.append(arr[l])
    r -=1
    l +=1

if len(arr) % 2 == 1:
    mid = len(arr)//2
    ans.append(arr[mid])
print(*ans)

    

