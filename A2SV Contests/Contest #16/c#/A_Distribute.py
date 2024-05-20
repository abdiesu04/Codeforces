n = int(input())
arr = list(map(int, input().split() ))
a = sorted(arr)
res = []
for i in range(n//2):
    res.append(str(arr.index(a[i])+1))
    arr[arr.index(a[i])] = 0
    res.append(str(arr.index(a[-(i+1)])+1))
    arr[arr.index(a[-(i+1)])] = 0
    print(" ".join(res))
    res.clear()