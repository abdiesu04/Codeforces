t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    s = input()
    xorPrefix = [0] * n
    xorPrefix[0] = arr[0]
    for i in range(1, n):
        xorPrefix[i] = xorPrefix[i-1] ^ arr[i]
    q = int(input())
    for _ in range(q):
        query, *args = map(int, input().split())
        if query == 1:
            l, r = args
            l -= 1 
            r -= 1
            if l > 0:
                xor_val = xorPrefix[r] ^ xorPrefix[l-1]
            else:
                xor_val = xorPrefix[r]
            for i in range(l, r+1):
           