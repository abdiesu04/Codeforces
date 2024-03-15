t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    ans = 0
    
 
    for i in range(n - 1):
        if s[i] == s[i + 1] or s[i] == '?' or s[i + 1] == '?':
            ans = 1
    

    for i in range(2, n):
        v = []
        for j in range(n - i):
            if s[j] == s[j + i] or s[j] == '?' or s[j + i] == '?':
                v.append(j)
        v.sort()

        mx = 1
        cnt = 1
        for j in range(1, len(v)):
            if v[j] - 1 == v[j - 1]:
                cnt += 1
            else:
                mx = max(mx, cnt)
                cnt = 1
        mx = max(mx, cnt)
        if mx >= i:
            ans = max(ans, i)
    
    print(2 * ans)