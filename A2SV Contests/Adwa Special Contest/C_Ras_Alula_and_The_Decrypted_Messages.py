def is_possible(s, w):
    n = len(s)
    m = len(w)
    
    if m > n:
        return False
    
    sum_s = sum(ord(ch) for ch in s[:m])
    sum_w = sum(ord(ch) for ch in w)
    
    if sum_s == sum_w:
        return True
    
    for i in range(m, n):
        sum_s += ord(s[i]) - ord(s[i - m])
        if sum_s == sum_w:
            return True
    
    return False


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    s = input()
    w = input()
    
    result = is_possible(s, w)
    print("YES" if result else "NO")