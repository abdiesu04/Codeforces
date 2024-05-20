n = int(input())
for _ in range(n):
    t = input()
    s = input()
    arr = [0] * len(s)
    for i in range(len(s)):
        if s[i] == '1':
            arr[i] = 1
        elif s[i] == '0':
            arr[i] = -1
    negs = 0
    pos = 0
    max_negs = 0
    max_pos = 0

    for i in range(len(arr)):
        if arr[i] == -1:
            negs += 1
            pos = 0
            max_negs = max(max_negs, negs)
        elif arr[i] == 1:
            pos += 1
            negs = 0
            max_pos = max(max_pos, pos)
            
    print(max(max_negs, max_pos))