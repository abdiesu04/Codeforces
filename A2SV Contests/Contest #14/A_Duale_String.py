


n = int(input())
for _ in range(n):
    s = input()
    if len(s) % 2 == 0 and s[:len(s)//2] == s[len(s)//2:]:
        print("YES")
    else:
        print("NO")
