t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    for i in range(len(s)-1):
        if s[i] == ')' and s[i+1] == '(':
            n -= 1
    print(n)