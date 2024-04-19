from math import gcd

def find_gcd(arr):
    result = arr[0]  
    for i in range(1, len(arr)):
        result = gcd(result, arr[i])  
    return result

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    for i in range(len(arr)):
        arr[i] -= k

    neg = pos = zeros = 0
    for i in arr:
        if i < 0:
            neg += 1
        elif i > 0:
            pos += 1
        else:
            zeros += 1
    if not (pos == n or neg == n or zeros == n):
        print(-1)
        continue

    gc = find_gcd(arr)
    if gc == 0:
        print(0)  
        continue
    
    for i in range(len(arr)):
    
        cnt += int(abs(arr[i] / gc) - 1)
    print(abs(cnt))